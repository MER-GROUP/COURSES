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
print(*_arr, sep='\n') # test
print('----------')
_min, _max = float('inf'), float('-inf')
_index_row, _index_col, _count = -1, -1, 0

step_row = step_col = max(n, m)

for row in range(step_row):
    # ----------------------------
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
    # ----------------------------
    print(f'_min = {_min}') # test
    print(f'index_col = {index_col}') # test
    # ----------------------------
    for col2 in range(step_row):
        for row2 in range(step_col):
            try:
                if _max < _arr[row2][col2]:
                    _max = _arr[row2][col2]
                    index_row = row2
                    _count = 0
                elif _max == _arr[row2][col2]:
                    index_row = row2
            except IndexError:
                pass
    # ----------------------------
        if _min == _max == _arr[index_row][index_col]:
            _count += 1
    # ----------------------------
    print(f'_max = {_max}') # test
    print(f'index_row = {index_row}') # test
    print('----------')
print(_count)