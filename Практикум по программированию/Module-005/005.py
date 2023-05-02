'''
Максимальный элемент массива
Напишите программу, которая находит значение максимального элемента массива.

Входные данные
В первой строке задается одно натуральное число N, 
не превосходящее 1000 – размер массива.

Во второй строке вводятся N чисел – элементы массива 
(целые числа, не превосходящие по модулю 1000).

Выходные данные
Вывести одно число – значение максимального элемента в массиве.

Sample Input:
5
1 2 3 4 5
Sample Output:
5
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='005.csv', mode='rt', encoding='utf-8', newline='')
nm, tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(nm)
# print(tup)
arr = array('i', map(int, tup.split()))
# print(arr)

# 1
print(max(arr))

# 2
_max = float('-inf')
for el in arr:
    _max = max(el, _max)
print(_max)