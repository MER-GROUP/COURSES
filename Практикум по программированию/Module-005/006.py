'''
Номер максимального элемента массива
Напишите программу, которая находит номер максимального элемента массива.

Входные данные
В первой строке задается одно натуральное число N, 
не превосходящее 1000 – размер массива.

Во второй строке вводится N чисел – элементы массива 
(целые числа, не превосходящие по модулю 1000).

Выходные данные
Вывести одно число – номер максимального элемента в массиве 
(номера элементов в массиве считаем начиная с единицы). 

Sample Input:
5
5 4 3 2 1
Sample Output:
1
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='006.csv', mode='rt', encoding='utf-8', newline='')
nm, tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(nm)
# print(tup)
arr = array('i', map(int, tup.split()))
# print(arr)

# 1
print(arr.index(max(arr)) + 1)

# 2
_max, _index = float('-inf'), -1
for i, el in enumerate(arr, 1):
    if _max < el:
        _max, _index = el, i
print(_index)