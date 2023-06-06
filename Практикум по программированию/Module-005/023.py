'''
Библиотечный метод
Продемонстрируйте работу метода сортировки вставками по возрастанию. 
Для этого выведите состояние данного массива после каждой вставки 
на отдельных строках. Если массив упорядочен изначально, то следует 
не выводить ничего.

Входные данные
На первой строке дано число (1 ≤ N ≤ 100) – количество элементов в массиве. 
На второй строке задан сам массив: последовательность натуральных чисел, 
не превышающих 10^9.

Выходные данные
В выходной файл выведите строки (по количеству вставок) по N чисел каждая.

Sample Input 1:
2
2 1
Sample Output 1:
1 2

Sample Input 2:
4
2 1 5 3
Sample Output 2:
1 2 5 3
1 2 3 5
'''
import sys
from array import array
from copy import copy

# sys.stdin = open(file='023.csv', mode='rt', encoding='utf-8', newline='')
_, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(tup)
arr = array('i', map(int, tup[0].split()))
# print(arr)

# def insert_sort(arr: list) -> None:
#     arr1 = copy(arr)
#     n = len(arr1)
#     for i in range(1, n):
#         insert_element = arr1[i]
#         j = i - 1
#         while (0 <= j) and (arr1[j] > insert_element):
#             arr1[j+1] = arr1[j]
#             j -= 1
#         arr1[j+1] = insert_element
#         print(*arr1)
# insert_sort(arr)

def buble_sort(arr: list) -> None:
    arr1 = copy(arr)
    n = len(arr1)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr1[j] > arr1[j+1]:
                arr1[j], arr1[j+1] = arr1[j+1],arr1[j]
                print(*arr1)
buble_sort(arr)