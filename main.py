from pprint import pprint
import re
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
print()
correct_list = []

for element in contacts_list: # Форматирование строк, чтобы привести их в нормальный вид
    row_list = []
    row = ','.join(element)
    pattern = '([А-ёA-Za-z]+)[,|\s]*([А-ёa-z]*)[,|\s]*([А-ёa-z]*)[,|\s]*([А-ёa-z]*)[,|\s]*([А-ёa-z\-\s]*)[,|\s]*([\+7|8|a-z]*[\s]*[\(]*[\d{3}]*[\)]*[\s|-]*[\d{3}]*[\s|-]*[\d{2}]*[\s|-]*[\d{2}]*)[,|\s]*[\(]*([а-ё.\s\d]*)[\)]*[,|\s]([0-9A-Za-z.]*[\.]*[A-Z]*[@]*[a-z.]*[a-z]*)'
    correct_row = re.sub(pattern, r"\1", row) # Форматирование делается отдельно, так как нужно получить список списков строк
    row_list.append(correct_row)
    correct_row = re.sub(pattern, r"\2", row)
    row_list.append(correct_row)
    correct_row = re.sub(pattern, r"\3", row)
    row_list.append(correct_row)
    correct_row = re.sub(pattern, r"\4", row)
    row_list.append(correct_row)
    correct_row = re.sub(pattern, r"\5", row)
    row_list.append(correct_row)
    correct_row = re.sub(pattern, r"\6", row)
    row_list.append(correct_row)
    correct_row = re.sub(pattern, r"(\7)", row)
    row_list.append(correct_row)
    correct_row = re.sub(pattern, r"\8", row)
    row_list.append(correct_row)
    correct_list.append(row_list)   
clear_dict = {} # Сюда добавляются уникальные элементы
check_dict = {} # Сюда добавляются элементы, которые есть в clear_dict, чтобы потом совместить их в одно целое
for element in correct_list: 
    key = element[0]
    element.remove(key)
    if key in clear_dict:
        help_dict = {key:element}
        check_dict.update(help_dict)
    else:
        help_dict = {key:element}
        clear_dict.update(help_dict)
for k, v in clear_dict.items():
    for replay, replay_value in check_dict.items():
        if k == replay:
            for element in v:
                if element == '':
                    v[v.index(element)] = replay_value[v.index(element)]
                if element == '': # Условие, о котором говорится строчкой ниже
                    try: # try нужен, так как без него алгоритм будет выдавать ошибку по причине отсутствия элемента с значением '' в списке, хотя условие выше он прошёл)
                        v[v.index(element)] = 'Null' # Пустой элемент заменяется, чтобы менялся индекс в методах v.index(element), так как если элементов '' несколько, то индекс меняться не будет
                    except:
                        pass
correct_list = []
for k, v in clear_dict.items(): # Формируем готовый список списков строк без '' и 'Null'
    help_list = []
    help_list.append(k)
    for element in v:
        if element == '' or element == 'Null' or element == '()':
            continue
        else:
            help_list.append(element)
    correct_list.append(help_list)
with open("phonebook.csv", "w") as f: # Записываем первый раз, чтобы потом взять оттуда текст в удобном формате и отформатировать оставшиеся номера
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(correct_list)
correct_list = []
with open("phonebook.csv") as f: # Открываем файл с нашим текстом
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    clear_list = []
for element in contacts_list:
    try:
        element[1] # Во время преобразования текста в списки, пустые строки преобразовались в пустые списки, этот код нужен для того, чтобы очистить общий список clear_list от таких пустых
        clear_list.append(element)
    except:
        continue
pattern = '[\+7|8|]+[\s\-]*[\(]*(\d{3})[\)]*[\s\-]*(\d{3})[\s\-]*(\d{2})[\s\-]*(\d{2})'
for element in clear_list: # Форматирование строк, чтобы привести их в нормальный вид
    row = ','.join(element)
    correct_row = re.sub(pattern, r"+7(\1)\2-\3-\4", row) # Форматирование делается отдельно, так как нужно получить список списков строк
    correct_list.append(correct_row.split(','))
with open("phonebook.csv", "w") as f: # Записываем текст с номерами
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(correct_list)