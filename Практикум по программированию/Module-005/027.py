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

if __name__ == '__main__':
    sys.stdin = open(file='027.csv', mode='rt', encoding='utf-8', newline='')
    n, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
    print(n)
    print(tup)
    # arr = array('i', map(int, tup[0].split()))
    # print(arr)