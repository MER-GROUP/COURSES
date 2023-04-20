'''
Заполнение диагоналями
Даны числа n и m. Создайте массив A[n][m] и заполните его, как показано на примере.

Входные данные
Программа получает на вход два числа n и m.

Выходные данные
Программа должна вывести  полученный массив, отводя на вывод каждого числа ровно 3 символа.

Sample Input:
4 10
Sample Output:
  0  1  3  6 10 14 18 22 26 30
  2  4  7 11 15 19 23 27 31 34
  5  8 12 16 20 24 28 32 35 37
  9 13 17 21 25 29 33 36 38 39
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
arr = [['.']*m for i in range(n)]
[print(*i) for i in arr]

pass