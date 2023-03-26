'''
Четные индексы
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).

Программа должна быть эффективной и не выполнять лишних действий!

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
1 2 3 4 5
Sample Output:
1 3 5
'''
import sys
from array import array

sys.stdin = open(file='016.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
print(arr) # test

pass