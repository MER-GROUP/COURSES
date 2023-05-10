'''
Приближенный двоичный поиск
Реализуйте алгоритм приближенного бинарного поиска.

Входные данные
В первой строке входных данных содержатся числа N и K (0 < N, K  < 100001). 
Во второй строке задаются N чисел первого массива, отсортированного по неубыванию, 
а в третьей строке – K чисел второго массива. Каждое число в обоих массивах 
по модулю не превосходит 2*10^9.

Выходные данные
Для каждого из K чисел выведите в отдельную строку число из первого массива, 
наиболее близкое к данному. Если таких несколько, выведите меньшее из них.

Sample Input:
5 5
1 3 5 7 9
2 4 8 1 6
Sample Output:
1
3
7
1
5
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='012.csv', mode='rt', encoding='utf-8', newline='')
_, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(_)
# print(tup)
arr1 = array('i', sorted(map(int, tup[0].split())))
# print(arr1)
arr2 = array('i', map(int, tup[1].split()))
# print(arr2)

# 1
for el in arr2:
    print(min(arr1, key=lambda x: abs(x-el)))
print('----------')

# 2
for el in arr2:
    left, right = 0, len(arr1)-1
    index = -1
    _min, _min_abs = float('inf'), float('inf') 
    while left <= right and -1 == index:
        mid = left + (right - left)//2
        if el == arr1[mid]:
            index = mid
        else:
            if abs(el-arr1[mid]) <= _min_abs:
                _min_abs = abs(el-arr1[mid])
                _min = arr1[mid]
            if el > arr1[mid]:
                left = mid + 1
                try:
                    if abs(el-arr1[left]) <= _min_abs:
                        _min_abs = abs(el-arr1[left])
                        _min = min(arr1[left], _min)
                except IndexError:
                    pass
            else:
                right = mid - 1
                try:
                    if abs(el-arr1[right]) <= _min_abs:
                        _min_abs = abs(el-arr1[right])
                        _min = min(arr1[right], _min)
                except IndexError:
                    pass
    print((arr1[index], _min)[-1 == index]) 