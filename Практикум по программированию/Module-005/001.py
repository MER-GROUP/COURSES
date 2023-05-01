'''
Линейный поиск - 1
Напишите программу, которая определяет, сколько раз встречается заданное 
число x в данном массиве.

Входные данные
В первой строке задается одно натуральное число N, 
не превосходящее 1000 – размер массива.

Во второй строке вводятся N чисел – элементы массива 
(целые числа, не превосходящие по модулю 1000).

В третьей строке содержится одно целое число x , 
не превосходящее по модулю 1000.

Выходные данные
Вывести одно число – сколько раз встречается x в данном массиве.

Sample Input:
5
1 2 3 4 5
3
Sample Output:
1
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='001.csv', mode='rt', encoding='utf-8', newline='')
nm, tup, digit = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(nm)
# print(tup)
digit = int(digit)
# print(digit)
arr = array('i', map(int, tup.split()))
# print(arr)

# 1
print(arr.count(digit))

# 2
print(sum(i==digit for i in arr))