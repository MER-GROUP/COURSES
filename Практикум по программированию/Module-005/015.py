'''
Левый и правый двоичный поиск
Дано два списка чисел, числа в первом списке упорядочены 
по неубыванию. Для каждого числа из второго списка определите 
номер первого и последнего появления этого числа в первом списке.

Входные данные
В первой строке входных данных записано два числа N и M (1 < N, M < 20000). 
Во второй строке записано N упорядоченных по неубыванию целых 
чисел — элементы первого списка. В третьей строке записаны M целых 
неотрицательных чисел - элементы второго списка. 
Все числа в списках - целые 32-битные знаковые.

Выходные данные
Программа должна вывести M строчек. Для каждого числа из второго 
списка нужно вывести номер его первого и последнего вхождения в первый 
список. Нумерация начинается с единицы. Если число не входит в первый 
список, нужно вывести одно число 0.

Sample Input:
10 5
1 1 3 3 5 7 9 18 18 57
57 3 9 1 179
Sample Output:
10 10
3 4
7 7
1 2
0
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='015.csv', mode='rt', encoding='utf-8', newline='')
_, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
print(tup)
arr1 = array('i', sorted(map(int, tup[0].split())))
print(arr1)
arr2 = array('i', map(int, tup[1].split()))
print(arr2)
print('----------')

# 0
for el in arr2:
    if el in arr1:
        print(arr1.index(el)+1, end=' ')
        print(abs(list(reversed(arr1)).index(el)-len(arr1)))
    else:
        print(0)
print('----------')

# 1
from bisect import bisect_left, bisect_right
for el in arr2:
    left = bisect_left(arr1, el)
    right = bisect_right(arr1, el)
    if left == right:
        print(0)
    else:
        print(left + 1, end=' ')
        print(right)
print('----------')

# 2
def binary_search_left(arr: list, el: int) -> int:
    left, right = 0, len(arr)
    while left < right:
            mid = left + (right-left)//2
            if arr[mid] < el:
                left = mid + 1
            else:
                right = mid
    return left

def binary_search_right(arr: list, el: int) -> int:
    left, right = 0, len(arr)
    while left < right:
            mid = left + (right-left)//2
            if arr[mid] > el:
                right = mid
            else:
                left = mid + 1
    return right

for el in arr2:
    left = binary_search_left(arr1, el)
    right = binary_search_right(arr1, el)
    if left == right:
         print(0)
    else:
        print(left + 1, end=' ')
        print(right)
print('----------')

# 3
def binary_search_left_rec(arr: list, el: int) -> int:
    _left, _right = 0, len(arr)
    def rec(left: int = _left, right: int = _right):
        mid = left + (right-left)//2
        if not left < right:
            return left
        elif arr[mid] < el:
            left = mid + 1
        else:
            right = mid
        return rec(left, right)
    return rec(_left, _right)

def binary_search_right_rec(arr: list, el: int) -> int:
    _left, _right = 0, len(arr)
    def rec(left: int = _left, right: int = _right):
        mid = left + (right-left)//2
        if not left < right:
            return right
        elif arr[mid] > el:
            right = mid
        else:
            left = mid + 1
        return rec(left, right)
    return rec(_left, _right)
         
for el in arr2:
    left = binary_search_left_rec(arr1, el)
    right = binary_search_right_rec(arr1, el)
    if left == right:
         print(0)
    else:
        print(left + 1, end=' ')
        print(right)
print('----------')