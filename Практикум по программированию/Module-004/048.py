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
print(n) # test
print(m) # test
# arr = [list(map(int, arr[i].split())) for i in range(n)]
# [print(*i) for i in arr]

pass