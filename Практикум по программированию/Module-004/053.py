'''
Сапер
Напишите программу, отображающую игровое поле для игры "Сапер".

Входные данные
Даны числа N и M (целые, положительные, не превышают 32) – количество строк 
и столбцов в поле соответственно, далее число 
W (целое, неотрицательное, не больше 1000) – количество мин на поле, 
далее следует W пар чисел, координаты мины 
на поле (первое число – строка, второе число – столбец).

Выходные данные
Требуется вывести на экран поле. Формат вывода указан в примере.

Правила игры Сапер
https://pcbee.ru/games/kak-igrat-v-sapera.html

Sample Input:
3 2
2
1 1
2 2
Sample Output:
* 2
2 *
1 1
'''
import sys
# from array import array
# from copy import copy

def bomb(arr: list, coords: tuple) -> None:
    # # O(2N)
    # n, m = len(arr), len(arr[0])
    # for i in range(n):
    #     for j in Wrange(m):
    #         coord = (i+1, j+1)
    #         if coord in coords:
    #             arr[i][j] = '*'

    # O(N)
    for x, y in coords:
        arr[x-1][y-1] = '*'

def digits(arr, i, j):
    _count = 0
    if '*' == arr[i][j]:
        return '*'
    i -= 1
    j -= 1
    n = 3
    for r in range(i, i+n):
        for c in range(j, + j+n):
            try:
                if -1 in (r, c):
                    raise IndexError
                if '*' == arr[r][c]:
                    _count += 1
            except IndexError:
                pass
    return _count

def help(arr):
    n, m = len(arr), len(arr[0])
    for i in range(n):
        for j in range(m):
            arr[i][j] = digits(arr, i, j)

sys.stdin = open(file='053.csv', mode='rt', encoding='utf-8', newline='')
nm, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
# nm = tuple(map(str.strip, sys.stdin.read().splitlines()))
# arr = array('i', list(map(int, arr.split())))
# n, m = map(int, nm[0].split())
n, m = map(int, nm.split())
# print(n) # test
# print(m) # test
# print(tup) # test
coords = tuple(tuple(map(int, i.split())) for i in tup[1:])
# print(coords)
# arr = [list(map(int, arr[i].split())) for i in range(n)]
arr = [[0]*m for i in range(n)]
# [print(*i) for i in arr]

if int(tup[0]):
    bomb(arr, coords)
    # [print(*i) for i in arr]
    help(arr)
[print(*i) for i in arr]