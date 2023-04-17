'''
Треугольник Паскаля
Даны два числа n и m. Создайте двумерный массив [n][m] и заполните 
его по следующим правилам: Числа, стоящие в строке 0 или в 
столбце 0 равны 1 (A[0][j]=1, A[i][0]=1). Для всех остальных 
элементов массива A[i][j]=A[i-1][j]+A[i][j-1], то есть каждый элемент 
равен сумме двух элементов, стоящих слева и сверху от него.

Входные данные
Программа получает на вход два числа n и m.

Выходные данные
Выведите данный массив.

Sample Input:
3 3
Sample Output:
1 1 1
1 2 3
1 3 6
'''
import sys
# from array import array
# from copy import copy

sys.stdin = open(file='049.csv', mode='rt', encoding='utf-8', newline='')
# nm, *arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
nm = tuple(map(str.strip, sys.stdin.read().splitlines()))
# arr = array('i', list(map(int, arr.split())))
n, m = map(int, nm[0].split())
print(n) # test
print(m) # test
# arr = [list(map(int, arr[i].split())) for i in range(n)]
# [print(*i) for i in arr]

arr = [[0]*m for _ in range(n)]
# [print(*i) for i in arr]
for i in range(n):
    for j in range(m):
        if 0 in (i, j):
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
[print(*i) for i in arr]