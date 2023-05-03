'''
Матрица
Задана матрица K, содержащая n строк и m столбцов. Седловой 
точкой этой матрицы назовем элемент, который одновременно является 
минимумом в своей строке и максимумом в своем столбце.

Найдите количество седловых точек заданной матрицы.

Входные данные
Первая строка содержит целые числа n и m (1 ≤ n, m ≤ 750). 
Далее следуют n строк по m чисел в каждой. j-ое число i-ой строки равно kij. 
Все kij по модулю не превосходят 1000.

Выходные данные
Выведите ответ на задачу.

Sample Input:
2 2
0 0
0 0
Sample Output:
4
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='009.csv', mode='rt', encoding='utf-8', newline='')
nm, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
print(nm)
print(tup)
# arr = array('i', map(int, tup.split()))
# print(arr)

# 1
pass