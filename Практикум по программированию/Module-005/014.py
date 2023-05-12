'''
Двоичный поиск
Реализуйте алгоритм бинарного поиска.

Входные данные
В первой строке входных данных содержатся натуральные 
числа N и K (0 < N, K < 100000). Во второй строке задаются 
N элементов первого массива, отсортированного по возрастанию, 
а в третьей строке – K элементов второго массива. Элементы 
обоих массивов - целые числа, каждое из которых по модулю не 
превосходит 10^9

Выходные данные
Требуется для каждого из K чисел вывести в отдельную строку "YES", 
если это число встречается в первом массиве, и "NO" в противном случае.

Sample Input:
10 5
1 2 3 4 5 6 7 8 9 10
-2 0 4 9 12
Sample Output:
NO
NO
YES
YES
NO
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='014.csv', mode='rt', encoding='utf-8', newline='')
_, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(tup)
arr1 = array('i', sorted(map(int, tup[0].split())))
# print(arr1)
arr2 = array('i', map(int, tup[1].split()))
# print(arr2)

# 1
from bisect import bisect
for el in arr2:
    print(('NO', 'YES')[el == arr1[bisect(arr1, el)-1]])
print('*****')

# 2
def bi_search(arr: list, el: int) -> int:
    index, left, right = -1, 0, len(arr)-1
    while left <= right and -1 == index:
        mid = left + (right-left)//2
        if el == arr[mid]: index = mid
        elif el < arr[mid]: right = mid-1
        else: left = mid+1
    return index

for el in arr2:
    print(('NO', 'YES')[-1 != bi_search(arr1, el)])
print('*****')

# 3
def bi_search_rec(arr: list, el: int) -> str:
    mid = (len(arr)-1)//2
    if 0 > mid: return 'NO'
    elif el == arr[mid]: return 'YES'
    elif 2 > len(arr): return 'NO'
    elif el < arr[mid]: return bi_search_rec(arr[:mid], el)
    else: return bi_search_rec(arr[mid+1:], el)

for el in arr2:
    print(bi_search_rec(arr1, el))
print('*****')