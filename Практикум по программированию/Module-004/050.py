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
digit = (2 * n + 1)**2 - 1
i = 0
j = 2 * n
up, right, left = [False] * 3
down = True

while True:
    # down
    if down:
        if -1 < i < (2*n+1) \
        and -1 < j < (2*n+1) \
        and '.' == arr[i][j]:
            arr[i][j] = digit
            digit -= 1
            i += 1  
        else:
            down = False
            left = True
            i -= 1
            j -= 1
            if -1 == digit: break
    # left
    if left:
        if -1 < i < (2*n+1) \
        and -1 < j < (2*n+1) \
        and '.' == arr[i][j]:
            arr[i][j] = digit
            digit -= 1
            j -= 1
        else:
            left = False
            up = True
            j += 1
            i -= 1
            if -1 == digit: break
    # up
    if up:
        if -1 < i < (2*n+1) \
        and -1 < j < (2*n+1) \
        and '.' == arr[i][j]:
            arr[i][j] = digit
            digit -= 1
            i -= 1
        else:
            up = False
            right = True
            i += 1
            j += 1
            if -1 == digit: break
    # right
    if right:
        if -1 < i < (2*n+1) \
        and -1 < j < (2*n+1) \
        and '.' == arr[i][j]:
            arr[i][j] = digit
            digit -= 1
            j += 1
        else:
            right = False
            down = True
            j -= 1
            i += 1
            if -1 == digit: break

for i in range(len(arr)):
    for j in range(len(arr)):
        print(str(arr[i][j]).rjust(3), end="")
    print()