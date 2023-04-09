'''
Большой сдвиг
Дан список из N (1≤N≤100000) целых чисел и число K (|K|<100000). 
Циклически сдвиньте список на |K| элементов вправо, 
если K – положительное и влево, если отрицательное число.

Входные данные
Программа получает на вход список целых чисел, затем число K.

Выходные данные
Выведите ответ на задачу.

Примечание
Решение должно иметь сложность O(N), то есть не должно зависеть от K. 
Дополнительным списком пользоваться нельзя.

Sample Input:
5 3 7 4 6
3
Sample Output:
7 4 6 5 3
'''
import sys
from array import array
from copy import copy

# sys.stdin = open(file='040.csv', mode='rt', encoding='utf-8', newline='')
arr, n = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr.split())))
n = int(n)
# print(arr) # test
# print(n) # test

# 1 - O(2N)
_arr = copy(arr)
for _ in range(abs(n)):
    if 0 < n:
        for i in range(len(_arr)-1):
            _arr[i], _arr[-1] = _arr[-1], _arr[i]
    else:
        for i in range(-1, -len(_arr), -1):
            _arr[i], _arr[0] = _arr[0], _arr[i]
print(*_arr)

# 2 - O(2N)
_arr2 = copy(arr)
for _ in range(abs(n)):
    if 0 < n:
        for i in range(-1, -len(_arr2), -1):
            _arr2[i-1], _arr2[i] = _arr2[i], _arr2[i-1]
    else:
        for i in range(len(_arr2)-1):
            _arr2[i], _arr2[i+1] = _arr2[i+1], _arr2[i]
print(*_arr2)

# 3 - O(N)
_arr3 = copy(arr)
_ost = abs(n) % len(_arr3) if abs(n) >= len(_arr3) else abs(n)
if 0 < n:
    _arr3 = _arr3[-_ost:] + _arr3[:-_ost]
elif 0 > n:
    _arr3 = _arr3[_ost:] + _arr3[:_ost]
print(*_arr3)