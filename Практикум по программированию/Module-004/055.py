'''
Спираль
Требуется заполнить массив размера N × N единичками по спирали 
(начиная с верхнего левого угла по часовой стрелке, см. пример).

Входные данные
С клавиатуры вводится число N (нечетное, натуральное и не превышающее 50).

Выходные данные
Требуется вывести на экран построенную спираль.

Sample Input:
7
Sample Output:
1111111
0000001
1111101
1000101
1011101
1000001
1111111
'''
import sys
# from array import array
# from copy import copy

sys.stdin = open(file='055.csv', mode='rt', encoding='utf-8', newline='')
nm, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(nm)
# print(tup)
# arr = array('i', list(map(int, arr.split())))
n, *m = map(int, nm.split())
# print(n)
# # arr = [list(map(int, tup[i].split())) for i in range(n)]
arr = [[0]*n for _ in range(n)]
# [print(*i, sep='') for i in arr]

_right = n
_down = n
_left = 0
_up = 0
_check_left = False
# _exit_left = n

while 0 < n:
    # right
    for j in range(_left, _right):
        arr[_up][j] = 1
    _right -= 1
    n -= 1
    if not n: break

    # down
    for i in range(_up, _down):
        arr[i][_right] = 1
    _right -= 1
    _down -= 1
    n -= 1
    if not n: break

    # left
    # if _check_left or 3 == _exit_left: 
    if _check_left: 
        _left += 1
    for j in range(_right, _left-1, -1):
        arr[_down][j] = 1
        _check_left = True
    _up += 1
    _down -= 1
    n -= 1
    if not n: break

    # up
    for i in range(_down, _up, -1):
        arr[i][_left] = 1
    _left += 1
    _up += 1
    n -= 1
    if not n: break

[print(*i, sep='') for i in arr]