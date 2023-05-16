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

# 1
from bisect import bisect_left, bisect_right
for el in arr2:
    # print((bisect_left(arr1, el)+1, 0)[el not in arr1], end=' ')
    # print((bisect_right(arr1, el), '')[el not in arr1])
    left, right, n = bisect_left(arr1, el), bisect_right(arr1, el), len(arr1)
    print(f'{(0, left+1)[left < n and el == arr1[left]]}', end=' ')
    print(f'{("", right)[right-1 < n and el == arr1[right-1]]}')
print('----------')

# 2
def binary_search_left(arr: list, el: int) -> int:
    left, right, index = 0, len(arr)-1, -1
    while left <= right and -1 == index:
        mid = left + (right-left)//2
        if el == arr[mid]: index = mid
        elif el > arr[mid]: left = mid+1
        else: right = mid-1
    # return index, left, right
    return (0, left+1)[left < len(arr)]

for el in arr2:
    print(binary_search_left(arr1, el))
print('----------')

# 10 10
# 3 4
# 7 7
# 1 2
# 0
