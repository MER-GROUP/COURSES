'''
Хипуй!

В этой задаче вам необходимо организовать структуру данных Heap для хранения целых чисел, 
над которой определены следующие операции:

a) Insert(k) – добавить в Heap число k (1 ≤  k ≤ 1000000) ;
b) Extract достать из Heap наибольшее число (удалив его при этом).

Входные данные

В первой строке содержится количество команд N (1 ≤  N ≤ 100000), далее следуют N команд, 
каждая в своей строке.  Команда может иметь  формат: “0 <число>” или “1”, обозначающий, 
соответственно, операции Insert(<число>) и Extract. Гарантируется, 
что при выполенении команды Extract в структуре находится по крайней мере один элемент.

Выходные данные

Для каждой команды извлечения необходимо отдельной строкой вывести число, полученное 
при выполнении команды Extract.

Sample Input:
2
0 10000
1

Sample Output:
10000
'''
import sys
from array import array
# from copy import copy

def heapify_max(arr: array, index: int, size: int) -> None:
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

def heap_max(arr: array) -> None:
    for i in reversed(range((len(arr)-1) // 2)):
        heapify_max(arr, i, len(arr))

def heap_max_sort(arr: array):
    for i in reversed(range(len(arr))):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_max(arr, 0, i)

def heap_max_insert(arr: array, el: int) -> None:
    arr.append(el)
    right = len(arr)-1
    while right and arr[right//2] < arr[right]:
        arr[right//2], arr[right] = arr[right], arr[right//2]
        right = right//2

def heap_max_extract(arr: array) -> int:
    arr[0], arr[-1] = arr[-1], arr[0]
    root = arr.pop()
    heapify_max(arr, 0, len(arr))
    return root

if __name__ == '__main__':
    sys.stdin = open(file='027.csv', mode='rt', encoding='utf-8', newline='')
    _, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
    # print(_)
    # print(tup)
    # arr = array('i', map(int, tup[0].split()))
    # print(arr)

    heap = list()
    for el in tup:
        arr = array('i', map(int, el.split()))
        if 0 == arr[0]:
            heap_max_insert(heap, arr[1])
        else:
            print(heap_max_extract(heap))

    # arr = [1, 2, 3, 4, 5]
    # print(arr)
    # heap_max(arr)
    # print(arr)
    # heap_max_insert(arr, 66)
    # print(arr)
    # print(heap_max_extract(arr))
    # print(arr)

    # arr = [1, 2, 3]
    # print(arr)
    # arr.append(None)
    # print(arr)