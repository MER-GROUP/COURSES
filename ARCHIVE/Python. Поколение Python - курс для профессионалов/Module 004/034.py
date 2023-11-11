'''
Студенты курса
Вам доступен файл students.json, содержащий список JSON-объектов, которые представляют 
данные о студентах некоторого курса:

[
   {
      "name": "Holly-Anne",
      "city": "Abilene",
      "age": 29,
      "progress": 85,
      "phone": "(802) 983-9126"
   },
   ...
]

Под «студентом» мы будем подразумевать один JSON-объект из этого списка. 
У студента имеются следующие атрибуты:

name — имя 
city — город проживания
age — возраст
progress — прогресс по курсу в процентах
phone— контактный номер

Напишите программу, которая определяет студентов, удовлетворяющих следующим условиям:

возраст 18 лет или более
прогресс по курсу 75% или более
Программа должна создать файл data.csv с двумя столбцами — name (имя) и phone (номер), 
и записать в него данные выбранных студентов, расположив их в лексикографическом порядке имён. 
В качестве разделителя в файле data.csv должна быть использована запятая.

Примечание 1. Гарантируется, что все студенты имеют различные имена.

Примечание 2. Начальная часть файла data.csv выглядит так:

name,phone
Cary,(580) 476-8517
Catarina,(237) 608-2757
Catherin,(876) 215-3666
...

Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/623073/students.json
https://stepik.org/media/attachments/lesson/623073/clue_students.txt

Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
'''
import json, csv

# with open(file='034-students.json', mode='rt', encoding='utf-8', newline='') as file_opener,\
with open(file='students.json', mode='rt', encoding='utf-8', newline='') as file_opener,\
    open(file='data.csv', mode='wt', encoding='utf-8', newline='') as file_writener:

    students_list_dicts = filter(
        lambda x: 18 <= int(x['age']) and 75 <= int(x['progress']),
        json.load(fp=file_opener)
    )

    fieldnames = ['name', 'phone']
    csv_writener = csv.writer(file_writener, delimiter=',', quoting=csv.QUOTE_NONE)
    csv_writener.writerow(fieldnames)
    csv_writener.writerows(
        [[d[fieldnames[0]], d[fieldnames[1]]] \
            for d in sorted(students_list_dicts, key=lambda x: x[fieldnames[0]])]
    )