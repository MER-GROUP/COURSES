'''
Заполнение змейкой
Даны числа n и m. Создайте массив A[n][m] и заполните его змейкой (см. пример).

Входные данные
Программа получает на вход два числа n и m.

Выходные данные
Программа должна вывести  полученный массив, отводя на вывод каждого числа ровно 3 символа.

Sample Input:
4 10
Sample Output:
  0  1  2  3  4  5  6  7  8  9
 19 18 17 16 15 14 13 12 11 10
 20 21 22 23 24 25 26 27 28 29
 39 38 37 36 35 34 33 32 31 30
'''
import sys
# from array import array
# from copy import copy

sys.stdin = open(file='051.csv', mode='rt', encoding='utf-8', newline='')
# nm, *arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
nm = tuple(map(str.strip, sys.stdin.read().splitlines()))
# arr = array('i', list(map(int, arr.split())))
n, m = map(int, nm[0].split())
print(n) # test
print(m) # test
# arr = [list(map(int, arr[i].split())) for i in range(n)]
arr = [[0]*m for i in range(n)]
[print(*i) for i in arr]

pass