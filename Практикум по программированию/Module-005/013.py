'''
Сложность двоичного поиска
Вася загадал число от 1 до N. За какое наименьшее количество 
вопросов (на которые Вася отвечает "да" или "нет") 
Петя может угадать Васино число?

Входные данные
Вводится одно число N

Выходные данные
Выведите наименьшее количество вопросов, которого 
гарантированно хватит Пете, чтобы угадать Васино число.

Sample Input:
5
Sample Output:
3
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='013.csv', mode='rt', encoding='utf-8', newline='')
tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
print(tup)
arr = array('i', range(1, int(tup[0])+1))
print(arr)

# 1
index, _count = -1, 0
left, right = 0, len(arr)-1
while left <= right and -1 == index:
    mid = left + (right-left)//2
    if int(tup[0])+1 == arr[mid]:
        index = arr[mid]
        _count += 1
    else:
        _count += 1
        if int(tup[0])+1 < arr[mid]:
            right = mid-1
        else:
            left = mid+1 
print(_count)

# 2
def bi_searce(_arr: list, _el: int) -> int:
    _count = 0
    def rec():
        ...
    rec()