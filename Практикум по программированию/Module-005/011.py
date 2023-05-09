'''
Контроперация
Хакер Василий получил доступ к классному журналу и хочет 
заменить все свои минимальные оценки на максимальные. 
Напишите программу, которая заменяет оценки Василия, 
но наоборот (все максимальные - на минимальные).

Входные данные
Дано количество оценок Василия (не больше 100), 
затем сами оценки.

Выходные данные
Требуется вывести исправленные оценки в том же порядке.

Sample Input:
5 1 3 3 3 4
Sample Output:
1 3 3 3 1
'''
import sys
# from array import array
# from copy import copy

sys.stdin = open(file='010.csv', mode='rt', encoding='utf-8', newline='')
nm, tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
print(nm)
print(tup)
# n, m = map(int, nm.split())
# print(n)
# print(m)
# arr = array('i', map(int, tup.split()))
# print(arr)

# 1
pass