'''
Матрица
Задана матрица K, содержащая n строк и m столбцов. Седловой 
точкой этой матрицы назовем элемент, который одновременно является 
минимумом в своей строке и максимумом в своем столбце.

Найдите количество седловых точек заданной матрицы.

Входные данные
Первая строка содержит целые числа n и m (1 ≤ n, m ≤ 750). 
Далее следуют n строк по m чисел в каждой. row-ое число i-ой строки равно kirow. 
Все kirow по модулю не превосходят 1000.

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
n, m = map(int, nm.split())
print(n)
print(m)
# arr = array('i', map(int, tup.split()))
# print(arr)

_arr = [list(map(int, el.split())) for el in tup]
print(_arr) # test
_min, _max = float('inf'), float('-inf')
_index_row, _index_col, _count = -1, -1, 0

step_row = step_col = max(n, m)

for row in range(step_row):
    for col in range(step_col):
        try:
            if _min > _arr[row][col]:
                _min = _arr[row][col]
                index_col = col
                _count = 0
            elif _min == _arr[row][col]:
                index_col = col
        except IndexError:
            pass
        # тритий цик надо
        # ----------------------------

        # ----------------------------
        try:
            if _max < _arr[col][row]:
                _max = _arr[col][row]
                index_row = row
                _count = 0
            elif _max == _arr[col][row]:
                index_row = row
        except IndexError:
            pass
    if _min == _max == _arr[row][col]:
        _count += 1
print(_count)