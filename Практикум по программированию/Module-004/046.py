'''
Состязания - 4
В метании молота состязается n спортcменов. Каждый из них сделал mбросков. 
Победитель определяется по лучшему результату. Определите количество 
участников состязаний, которые разделили первое место, то есть определите 
количество строк в массиве, которые содержат значение, равное наибольшему.

Входные данные
Программа получает на вход два числа n и m, являющиеся числом строк 
и столбцов в массиве. Далее во входном потоке идет n строк по m чисел, 
являющихся элементами массива.

Выходные данные
Программа должна вывести  одно число - количество победителей соревнования.

Sample Input:
3 3
3 1 2
1 3 4
3 3 3
Sample Output:
1
'''
import sys
# from array import array
# from copy import copy

# sys.stdin = open(file='046.csv', mode='rt', encoding='utf-8', newline='')
nm, *arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
# arr = array('i', list(map(int, arr.split())))
n, m = map(int, nm.split())
# print(n) # test
# print(m) # test
arr = [list(map(int, arr[i].split())) for i in range(n)]
# [print(*i) for i in arr]

_max = float('-inf')
_count = 0
_i_prev = None
for i in range(n):
    for j in range(m):
        if _max < arr[i][j]:
            _max = arr[i][j]
            _count = 1
            _i_prev = i
        elif _max == arr[i][j]:
            if not i == _i_prev:
                _count += 1
                _i_prev = i
print(_count)