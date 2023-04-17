'''
Таблица умножения
Даны два числа n и m. Создайте двумерный массив A[n][m], заполните 
его таблицей умножения A[i][j]=i*j и выведите на экран. 
При этом нельзя использовать вложенные циклы, все заполнение массива 
должно производиться одним циклом.

Входные данные
Программа получает на вход два числа n и m – количество строк и столбцов, 
соответственно.

Выходные данные
Программа должна вывести  полученный массив. Числа разделяйте одним пробелом.

Sample Input:
3 3
Sample Output:
0 0 0
0 1 2
0 2 4
'''
import sys
# from array import array
# from copy import copy

sys.stdin = open(file='048.csv', mode='rt', encoding='utf-8', newline='')
# nm, *arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
nm = tuple(map(str.strip, sys.stdin.read().splitlines()))
# arr = array('i', list(map(int, arr.split())))
n, m = map(int, nm[0].split())
# print(n) # test
# print(m) # test
# arr = [list(map(int, arr[i].split())) for i in range(n)]
# [print(*i) for i in arr]

# 1
arr = list()
for i in range(n):
    _arr = list()
    for j in range(m):
        _arr.append(i*j)
    arr.append(_arr)
[print(*i) for i in arr]

# 2
arr = list()
_arr = list()
_i, _j = 0, 0
for _ in range(n*m):
    if not 0 == _ and not _ % m:
        _i += 1
        _j = 0
        arr.append(_arr.copy())
        _arr.clear()
    _arr.append(_i*_j)
    _j += 1
arr.append(_arr.copy())
_arr.clear()
[print(*i) for i in arr]

# 3
a = []
for k in range(n * m):
    i, j = divmod(k, m)
    if not j:
        row = [0] * m
        a.append(row)            
    row[j] = i * j
for row in a:
    print(*row) 

# 4
curr_num, add = 0, 0
for i in range(n*m):
    if not i % m and i:
        add += 1
        curr_num = add
        print('\n0', end='')
    else:
        print(f"{' ' * bool(i)}{curr_num}", end='')
        curr_num += add