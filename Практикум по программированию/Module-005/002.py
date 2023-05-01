'''
Линейный поиск - 2
Напишите программу, которая определяет, встречается ли заданное 
число x в данном массиве.

Входные данные
В первой строке задается одно натуральное число N, 
не превосходящее 1000 – размер массива.

Во второй строке вводятся N чисел – элементы 
массива (целые числа, не превосходящие по модулю 1000).

В третьей строке содержится одно целое число x, 
не превосходящее по модулю 1000.

Выходные данные
Вывести YES , если число x встречается в данном массиве, 
и NO в противном случае.

Sample Input:
5
1 2 3 4 5
3
Sample Output:
YES
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='002.csv', mode='rt', encoding='utf-8', newline='')
nm, tup, digit = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(nm)
# print(tup)
digit = int(digit)
# print(digit)
arr = array('i', map(int, tup.split()))
# print(arr)

# 1
try:
    print(('YES')[bool(arr.index(digit))])
except ValueError:
    print('NO')

# 2
print(('NO', 'YES')[any(filter(lambda x: x == digit, arr))])

# 3
_bool = 'NO'
for i in arr:
    if i == digit:
        _bool = "YES"
        break
print(_bool)