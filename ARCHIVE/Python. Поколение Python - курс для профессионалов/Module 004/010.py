'''
Grades

Вам доступен csv файл grades.csv, имеющий следующее содержание:

name;grade
Timur;100
Ruslan;97

Ниже представлена программа, которая должна открывать данный файл 
и выводить содержимое каждой строки в виде списка. 
В программе допущена ошибка, поэтому она выводит:

['n']
['a']
['m']
['e']
['', '']
['g']
['r']
['a']
['d']
['e']
[]
['T']
...

Найдите и исправьте ее, чтобы результатом работы программы были строки:

['name', 'grade']
['Timur', '100']
['Ruslan', '97']

Программа

import csv

with open('grades.csv', encoding='utf-8') as csv_file:
    # считываем содержимое файла
    text = csv_file.read()
    # создаем reader объект и указываем в качестве разделителя символ ;
    rows = csv.reader(text, delimiter=';')
    # выводим каждую строку
    for row in rows:
        print(row)
'''
import csv

with open('grades.csv', encoding='utf-8') as csv_file:
    # создаем reader объект и указываем в качестве разделителя символ ;
    rows = csv.reader(csv_file, delimiter=';')
    # выводим каждую строку
    for row in rows:
        print(row)