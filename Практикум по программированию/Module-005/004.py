'''
Линейный поиск - 3
Напишите программу, которая выводит номера элементов массива, 
равных данному числу.

Входные данные
В первой строке задается одно натуральное число N, 
не превосходящее 1000 – размер массива.

Во второй строке вводятся N чисел – элементы массива 
(целые числа, не превосходящие по модулю 1000).

В третьей строке содержится одно целое число x, 
не превосходящее по модулю 1000.

Выходные данные
Вывести через пробел номера элементов, равных данному, 
в порядке возрастания. Если таких элементов нет, 
ничего выводить не нужно.

Sample Input:
5
1 2 3 4 5
3
Sample Output:
3
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='004.csv', mode='rt', encoding='utf-8', newline='')
nm, tup, digit = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(nm)
# print(tup)
digit = int(digit)
# print(digit)
arr = array('i', map(int, tup.split()))
# print(arr)

for i, el in enumerate(arr, 1):
    if el == digit:
        print(i, end=' ')
print()