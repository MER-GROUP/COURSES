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
    left, right, n = bisect_left(arr1, el), bisect_right(arr1, el), len(arr1)
    print(f'{(0, left+1)[left < n and el == arr1[left]]}', end=' ')
    print(f'{("", right)[right-1 < n and el == arr1[right-1]]}')
print('----------')

# 2
def binary_search_left(arr: list, el: int) -> int:
    left, right = 0, len(arr)-1
    while left < right:
            mid = left + (right-left)//2
            if arr[mid] < el:
                left = mid + 1
            else:
                right = mid - 1
    return (0, left + 1)[el == arr[left]]

def binary_search_right(arr: list, el: int) -> int:
    left, right = 0, len(arr)-1
    while left < right:
            mid = left + (right-left)//2
            if arr[mid] > el:
                right = mid - 1
            else:
                left = mid + 1
    return ("", right + 1)[el == arr[right]]

for el in arr2:
    print(binary_search_left(arr1, el), end=' ')
    print(binary_search_right(arr1, el))
print('----------')

# 3
def binary_search_left_rec(arr: list, el: int) -> int:
    _left, _right = 0, len(arr)-1
    def rec(left: int = _left, right: int = _right):
        mid = left + (right-left)//2
        if not left < right:
            return left-2 if left > right else left-1\
                            if arr[left-1] == el else left
        elif arr[mid] > el:
            right = mid - 1
        else:
            left = mid + 1
        return rec(left, right)
    return rec(_left, _right)

def binary_search_right_rec(arr: list, el: int) -> int:
    _left, _right = 0, len(arr)-1
    def rec(left: int = _left, right: int = _right):
        mid = left + (right-left)//2
        if not left < right:
            return right
        elif arr[mid] == el:
            return right-2 if left < right and arr[right] != el else right
        elif arr[mid] < el:
            left = mid + 1
        else:
            right = mid - 1
        return rec(left, right)
    return rec(_left, _right)
         

for el in arr2:
    print((0, binary_search_left_rec(arr1, el)+1)[el == arr1[binary_search_left_rec(arr1, el)]], end=' ')
    print(("", binary_search_right_rec(arr1, el)+1)[el == arr1[binary_search_right_rec(arr1, el)]])
print('----------')