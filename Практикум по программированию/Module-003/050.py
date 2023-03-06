'''
Личные дела
Однажды, неловкая секретарша перепутала личные дела учащихся. 
Теперь их снова необходимо упорядочить сначала по классам, 
а внутри класса по фамилиям

Входные данные
В первой строке дано число N (1 ≤ N ≤ 1000) – количество личных дел. 
Далее для каждого из N учащихся следующие данные (каждое в своей строке): 
фамилия и имя, класс, дата рождения. Фамилия и имя – строки не более чем 
из 20 символов, класс – строка состоящая из числа (от 1 до 11) и 
латинской буквы (от "A" до "Z" ), дата рождения – дата в формате "ДД.ММ.ГГ" . 
Гарантируется, что внутри одного класса нет однофамильцев.

Выходные данные
В выходной файл требуется вывести N строк, в каждой из которых записаны 
данные по одному учащемуся. Строки должны быть упорядочены сначала 
по классам, а затем по фамилиям.

Sample Input:
3
Sidorov
Sidor
9A
20.07.93
Petrov
Petr
9B
23.10.92
Ivanov
Ivan
9A
10.04.93
Sample Output:
9A Ivanov Ivan 10.04.93
9A Sidorov Sidor 20.07.93
9B Petrov Petr 23.10.92
'''
import sys
from collections import namedtuple, defaultdict
student = namedtuple('student', ('surname' ,'name', 'classx', 'birthday'))
from statistics import mean

# sys.stdin = open(file='050.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = map(str.strip, sys.stdin.read().splitlines())
# print(*arr, sep='\n') # test

arr_new = list()
tmp = list()
for i, el in enumerate(arr):
    if not i % 4 and not 0 == i:
        arr_new.append(student._make(tmp))
        tmp.clear()
    tmp.append(el)
    if i == len(arr) - 1:
        arr_new.append(student._make(tmp))
# print(*arr_new) # test

[print(s.classx, s.surname, s.name, s.birthday) for s in sorted(
        arr_new, key=lambda x: (int(x.classx[:-1]), x.classx[-1], x.surname)
    )]