'''
Состязания - 3
В метании молота состязается n спортcменов. Каждый из них сделал mбросков. 
Побеждает спортсмен, у которого максимален наилучший бросок. 
Если таких несколько, то из них побеждает тот, у которого наилучшая 
сумма результатов по всем попыткам. Если и таких несколько, победителем 
считается спортсмен с минимальным номером. Определите номер победителя соревнований.

Входные данные
Программа получает на вход два числа n и m, являющиеся числом строк 
и столбцов в массиве. Далее во входном потоке идет n строк по m чисел, 
являющихся элементами массива.

Выходные данные
Программа должна вывести одно число - номер победителя соревнований. 
Не забудьте, что  строки  (спортсмены) нумеруются с 0.

Sample Input:
3 3
1 2 7
1 3 5
4 1 6
Sample Output:
0
'''
import sys
# from array import array
# from copy import copy

# sys.stdin = open(file='045.csv', mode='rt', encoding='utf-8', newline='')
nm, *arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
# arr = array('i', list(map(int, arr.split())))
n, m = map(int, nm.split())
# print(n) # test
# print(m) # test
arr = [list(map(int, arr[i].split())) for i in range(n)]
# [print(*i) for i in arr]

_index_i = int()
_max_n = float('-inf')
_max_sum = float('-inf')
for i, el in enumerate(arr):
    if _max_n < max(el):
        _max_n = max(el)
        _max_sum = sum(el)
        _index_i = i
    elif _max_n == max(el) and _max_sum < sum(el):
        _max_sum = sum(el)
        _index_i = i
print(f'{_index_i}')