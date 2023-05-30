'''
Пузырьковая сортировка_0
Требуется отсортировать массив по неубыванию методом "пузырька".

Входные данные
В первой строке вводится одно натуральное число, не превосходящее 1000 – размер массива. 
Во второй строке задаются N чисел – элементы массива 
(целые числа, не превосходящие по модулю 1000).

Выходные данные
Вывести получившийся массив.

Sample Input:
5
5 4 3 2 1
Sample Output:
1 2 3 4 5
'''
import sys
from array import array
from copy import copy

# sys.stdin = open(file='020.csv', mode='rt', encoding='utf-8', newline='')
_, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(tup)
arr1 = array('i', map(int, tup[0].split()))
# print(arr1)

# 1
print(*sorted(arr1))

# 2
arr2 = copy(arr1)
def buble_sort(arr2):
    n = len(arr2)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr2[j] > arr2[j+1]:
                arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
buble_sort(arr2)
print(*arr2)