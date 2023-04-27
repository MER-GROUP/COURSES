'''
Послезавтра
По заданной дате требуется определить, какое число будет послезавтра.

Напомним, что год является високосным, если его номер кратен 4, 
но не кратен 100, а также если он кратен 400.

Входные данные
Дано число, месяц и год (год  – число в промежутке от 1 до 10000).

Выходные данные
Требуется вывести, какое число будет послезавтра, в формате входных данных.

Sample Input:
1 8 2009
Sample Output:
3 8 2009
'''
import sys
# from array import array
# from copy import copy

sys.stdin = open(file='057.csv', mode='rt', encoding='utf-8', newline='')
nm, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
print(nm)
# print(tup)
# arr = array('i', list(map(int, arr.split())))
# n, *m = map(int, nm.split())
# print(n)
# # arr = [list(map(int, tup[i].split())) for i in range(n)]
# arr = [[0]*n for _ in range(n)]
# [print(*i, sep='') for i in arr]

pass