'''
Ближайшее число
Напишите программу, которая находит в массиве элемент, 
самый близкий по величине к  данному числу.

Входные данные
В первой строке задается одно натуральное число N, 
не превосходящее 1000 – размер массива.

Во второй строке содержатся N чисел – элементы массива 
(целые числа, не превосходящие по модулю 1000).

В третьей строке вводится одно целое число x, 
не превосходящее по модулю 1000.

Выходные данные
Вывести значение элемента массива, ближайшее к x. 
Если таких чисел несколько, выведите любое из них.

Sample Input:
5
1 2 3 4 5
6
Sample Output:
5
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='003.csv', mode='rt', encoding='utf-8', newline='')
nm, tup, digit = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(nm)
# print(tup)
digit = int(digit)
# print(digit)
arr = array('i', map(int, tup.split()))
# print(arr)

# 1
print(min(arr, key=lambda x: abs(x-digit)))

# 2
_min = __import__("math").inf
_el = None
for el in arr:
    if _min > abs(el - digit):
        _min = abs(el - digit)
        _el = el
print(_el)