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
from bisect import bisect, bisect_right, insort_left, bisect_left, insort_right, insort
print(bisect(arr, int(tup[0])))
print(bisect_right(arr, int(tup[0])))
print(bisect_left(arr, int(tup[0])))
print(insort(arr, int(tup[0])))
print(insort_left(arr, int(tup[0])))
print(insort_right(arr, int(tup[0])))