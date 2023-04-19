'''
Заполнение спиралью
Дано число n. Создайте массив A[2*n+1][2*n+1] и заполните его 
по спирали, начиная с числа 0 в центральной клетке A[n+1][n+1]. 
Спираль выходит вверх, далее закручивается против часовой стрелки.

Входные данные
Программа получает на вход одно число n.

Выходные данные
Программа должна вывести  полученный массив, отводя на вывод 
каждого числа ровно 3 символа.

Sample Input:
2
Sample Output:
 12 11 10  9 24
 13  2  1  8 23
 14  3  0  7 22
 15  4  5  6 21
 16 17 18 19 20
'''
import sys
# from array import array
# from copy import copy

sys.stdin = open(file='050.csv', mode='rt', encoding='utf-8', newline='')
# nm, *arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
nm = tuple(map(str.strip, sys.stdin.read().splitlines()))
# arr = array('i', list(map(int, arr.split())))
n, *m = map(int, nm[0].split())
# print(n) # test
# print(m) # test
# arr = [list(map(int, arr[i].split())) for i in range(n)]
# [print(*i) for i in arr]

arr = [['.'] * (2*n+1) for i in range(2*n+1)]
# [print(*i) for i in arr] # test
digit = (2 * n + 1)**2 - 1
# print(digit) # test
i = 0
j = 2 * n
# print(f'i = {i}, j = {j}') # test
up, right, left = [False] * 3
down = True
# print(f'up = {up}, right = {right}, left = {left}, down = {down}') # test

while True:
    # print('while') ##################

    # down
    if down:
        if -1 < i < (2*n+1) \
        and -1 < j < (2*n+1) \
        and '.' == arr[i][j]:
            print('down ###################') ###############################
            print(f'i = {i}, j = {j}') ###################
            arr[i][j] = digit
            digit -= 1
            i += 1  
        else:
            down = False
            left = True
            i -= 1
            j -= 1
            if 0 == digit: break
            print('111111111111111111') ##################
            print(f'i = {i}, j = {j}') ###################

    # left
    if left:
        if -1 < i < (2*n+1) \
        and -1 < j < (2*n+1) \
        and '.' == arr[i][j]:
            print('left ###################') ###############################
            print(f'i = {i}, j = {j}') ###################
            arr[i][j] = digit
            digit -= 1
            j -= 1
        else:
            left = False
            up = True
            j += 1
            i -= 1
            if 0 == digit: break
            print('222222222222222222') ##################
            print(f'i = {i}, j = {j}') ###################

    # up
    if up:
        if -1 < i < (2*n+1) \
        and -1 < j < (2*n+1) \
        and '.' == arr[i][j]:
            print('up ###################') ###############################
            print(f'i = {i}, j = {j}') ###################
            arr[i][j] = digit
            digit -= 1
            i -= 1
        else:
            up = False
            right = True
            i += 1
            j += 1
            if 0 == digit: break
            print('3333333333333333333') ##################
            print(f'i = {i}, j = {j}') ###################

    # right
    if right:
        if -1 < i < (2*n+1) \
        and -1 < j < (2*n+1) \
        and '.' == arr[i][j]:
            print('right ###################') ###############################
            print(f'i = {i}, j = {j}') ###################
            arr[i][j] = digit
            digit -= 1
            j += 1
        else:
            right = False
            down = True
            j -= 1
            i += 1
            if 0 == digit: break
            print('4444444444444444444') ##################
            print(f'i = {i}, j = {j}') ###################
[print(*i) for i in arr] # test