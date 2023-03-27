'''
Наибольший элемент
Дан список чисел. Выведите значение наибольшего элемента в списке, 
а затем индекс этого элемента в списке. Если наибольших элементов несколько, 
выведите индекс первого из них.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
1 2 3 2 1
Sample Output:
3 2
'''
import sys
from array import array

# sys.stdin = open(file='022.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

# print(max(arr), arr.index(max(arr))) # 1

# 2
_max = float('-inf')
_index = float('-inf')
for _i, _el in enumerate(arr):
    if _max < _el:
        _max = _el
        _index = _i
print(_max, _index)