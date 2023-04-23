'''
Переворот
Дан массив N × M. Требуется повернуть его по часовой стрелке на 90 градусов.

Входные данные
На первой строке даны натуральные числа N и M (1 ≤ N, M ≤ 50). 
На следующих N строках записано по M неотрицательных чисел, 
не превышающих 109 – сам массив.

Выходные данные
Выведите повернутый массив в формате входных данных.

Sample Input:
3 4
1 2 3 4
5 6 7 8
9 10 11 12
Sample Output:
9 5 1
10 6 2
11 7 3
12 8 4
'''
import sys
# from array import array
# from copy import copy

sys.stdin = open(file='054.csv', mode='rt', encoding='utf-8', newline='')
nm, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
# nm = tuple(map(str.strip, sys.stdin.read().splitlines()))
# arr = array('i', list(map(int, arr.split())))
# n, m = map(int, nm[0].split())
n, m = map(int, nm.split())
# print(n) # test
# print(m) # test
# print(tup) # test
arr = [list(map(int, tup[i].split())) for i in range(n)]
# [print(*i) for i in arr]

# 1
[print(*reversed(i)) for i in zip(*arr)]

# 2
arr2 = [[0]*n for _ in range(m)]
for i in range(n):
    for j in range(m):
        arr2[j][i] = arr[n-i-1][j]
[print(*i) for i in arr2]