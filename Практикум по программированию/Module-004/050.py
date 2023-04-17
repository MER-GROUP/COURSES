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
print(n) # test
print(m) # test
# arr = [list(map(int, arr[i].split())) for i in range(n)]
# [print(*i) for i in arr]

pass