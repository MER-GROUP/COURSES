'''
Пирамидальная сортировка
Отсортируйте данный массив. Используйте пирамидальную сортировку.

Входные данные
Первая строка входных данных содержит количество элементов 
в массиве N,  N  ≤  105. Далее задаются N целых чисел, 
не превосходящих по абсолютной величине 109.

Выходные данные
Выведите эти числа в порядке неубывания.

Sample Input:
5
5 4 3 2 1
Sample Output:
1 2 3 4 5
'''
import sys
from array import array
# from copy import copy

def heapify_max(arr: array, index: int, size: int):
    parrent = index
    left = 2*index + 1
    right = 2*index + 2

    if left < size and arr[left] > arr[parrent]:
        parrent = left
    if right < size and arr[right] > arr[parrent]:
        parrent = right
    if not parrent == index:
        arr[index], arr[parrent] = arr[parrent], arr[index]
        heapify_max(arr, parrent, size)

def heap_max(arr: array):
    for i in reversed(range((len(arr)-1) // 2)):
        heapify_max(arr, i, len(arr))

def heap_max_sort(arr: array):
    for i in reversed(range(len(arr))):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_max(arr, 0, i)

if __name__ == '__main__':
    sys.stdin = open(file='026.csv', mode='rt', encoding='utf-8', newline='')
    _, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
    # print(tup)
    arr = array('i', map(int, tup[0].split()))
    # print(arr)

    heap_max(arr)
    # print(arr) # test
    heap_max_sort(arr)
    print(*arr)

    # print(list((range(len(arr))))) # test
    # print(list(reversed(range(len(arr))))) # test
    # print(list(reversed(range(len(arr)-1)))) # test