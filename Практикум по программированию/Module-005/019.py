'''
Сортировка вставками
Требуется отсортировать массив по неубыванию методом "вставок".

Входные данные
В первой строке вводится одно натуральное число, 
не превосходящее 1000 – размер массива. Во второй строке 
задаются N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).

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

# sys.stdin = open(file='019.csv', mode='rt', encoding='utf-8', newline='')
_, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(tup)
arr1 = array('i', map(int, tup[0].split()))
# print(arr1)

# 1
print(*sorted(arr1))

# 2
arr2 = copy(arr1)
def insert_sort(arr):
    for i in range(1, len(arr)):
        insert_el = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > insert_el:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = insert_el
insert_sort(arr2)
print(*arr2)