'''
Сортировка выбором максимума
Требуется отсортировать массив по неубыванию методом "выбор максимума".

Входные данные
В первой строке вводится одно натуральное число N, 
не превосходящее 1000 – размер массива. Во второй строке 
задаются N чисел – элементы массива (целые числа, 
не превосходящие по модулю 1000).

Выходные данные
Вывести получившийся массив.

Sample Input:
2
3 1
Sample Output:
1 3
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='017.csv', mode='rt', encoding='utf-8', newline='')
_, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(tup)
arr1 = array('i', map(int, tup[0].split()))
# print(arr1)

# 1
print(*sorted(arr1))

# 2
n = len(arr1)
for i in range(n-1):
    _min_index = i
    for j in range(1+i, n):
        if arr1[j] < arr1[_min_index]:
            _min_index = j
    arr1[i], arr1[_min_index] = arr1[_min_index], arr1[i]
print(*arr1)