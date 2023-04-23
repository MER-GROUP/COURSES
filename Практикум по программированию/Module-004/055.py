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
print(nm)
print(tup)
# arr = array('i', list(map(int, arr.split())))
n, *m = map(int, nm.split())
print(n)
# # arr = [list(map(int, tup[i].split())) for i in range(n)]
arr = [[0]*n for _ in range(n)]
[print(*i, sep='') for i in arr]

pass