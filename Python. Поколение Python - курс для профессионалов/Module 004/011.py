'''
Writing Test

При попытке выполнить приведенную ниже программу возникает ошибка. Найдите и исправьте ее, чтобы программа создала файл writing_test.csv, имеющий следующее содержание:

first_col,second_col
value1,value2

Программа

import csv

with open('writing_test.csv', 'w', encoding='utf-8') as csv_file:
    # создаем writer объект и указываем названия столбцов
    writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
    # записываем первую строку с названиями столбцов
    writer.writeheader()
    # записываем строку с данными
    writer.writerow({'key1': 'value1', 'key2': 'value2'})
'''
import csv

with open('writing_test.csv', 'w', encoding='utf-8') as csv_file:
    # создаем writer объект и указываем названия столбцов
    writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
    # записываем первую строку с названиями столбцов
    writer.writeheader()
    # записываем строку с данными
    writer.writerow({'key1': 'value1', 'key2': 'value2'})