'''
Состязания - 5
В метании молота состязается n спортcменов. Каждый из них сделал m бросков. 
Победитель определяется по лучшему результату. Определите количество участников, 
а так же самих участников состязаний, которые разделили первое место, 
то есть определите количество строк в массиве, которые содержат значение, 
равное наибольшему.

Входные данные
Программа получает на вход два числа n и m, являющиеся числом строк и столбцов 
в массиве. Далее во входном потоке идет n строк по m чисел, являющихся элементами 
массива.

Выходные данные
Сначала программа выводит количество спортсменов, показавших наилучший результат, 
затем, на следующей строке, их номера в порядке возрастания (через пробел). 
Не забудьте, что  строки (спортсмены)  нумеруются с 0.

Sample Input:
3 3
3 1 2
1 3 4
3 3 3
Sample Output:
1
1
'''
import sys
# from array import array
# from copy import copy

# sys.stdin = open(file='047.csv', mode='rt', encoding='utf-8', newline='')
nm, *arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
# arr = array('i', list(map(int, arr.split())))
n, m = map(int, nm.split())
# print(n) # test
# print(m) # test
arr = [list(map(int, arr[i].split())) for i in range(n)]
# [print(*i) for i in arr]

_max_n = float('-inf')
_count_i = 0
_prev_i = None
_hist_i = str()
for i in range(n):
    for j in range(m):
        if _max_n < arr[i][j]:
            _max_n = arr[i][j]
            _count_i = 1
            _prev_i = i
            _hist_i = str(i) + ' '
        elif _max_n == arr[i][j] and not i == _prev_i:
                _count_i += 1
                _prev_i = i
                _hist_i += str(i) + ' '
print(_count_i)
print(_hist_i)