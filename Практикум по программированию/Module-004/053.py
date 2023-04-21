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

sys.stdin = open(file='053.csv', mode='rt', encoding='utf-8', newline='')
nm, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
# nm = tuple(map(str.strip, sys.stdin.read().splitlines()))
# arr = array('i', list(map(int, arr.split())))
# n, m = map(int, nm[0].split())
n, m = map(int, nm.split())
print(n) # test
print(m) # test
print(tup) # test
# arr = [list(map(int, arr[i].split())) for i in range(n)]
arr = [['.']*m for i in range(n)]
[print(*i) for i in arr]

pass