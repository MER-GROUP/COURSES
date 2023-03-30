'''
Циклический сдвиг вправо
Циклически сдвиньте элементы списка вправо (A[0] переходит на место A[1], 
A[1] на место A[2], ..., последний элемент переходит на место A[0]).

Используйте минимально возможное количество операций присваивания.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
1 2 3 4 5
Sample Output:
5 1 2 3 4
'''
import sys
from array import array
# from copy import copy

# sys.stdin = open(file='029.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

print(arr[-1], *arr[:-1]) # 1

# # 2
# _arr = copy(arr)
# for i in range(len(_arr)-1):
#     _arr[i], _arr[-1] = _arr[-1], _arr[i]
# print(*_arr)

# # 3
# _arr2 = copy(arr)
# for i in range(len(_arr2)-1, 0, -1):
#     _arr2[i], _arr2[i-1] = _arr2[i-1], _arr2[i]
# print(*_arr2)