'''
Максимальный - вперед
Требуется поменять местами первый элемент массива с максимальным.

Входные данные
В первой строке вводится одно натуральное число, 
не превосходящее 1000 – размер массива. Во второй строке 
задаются N чисел – элементы массива (целые числа, 
не превосходящие по модулю 1000).

Выходные данные
Вывести получившийся массив. Если максимальных элементов несколько, 
требуется поменять первый из них.

Sample Input:
5
1 2 3 4 5
Sample Output:
5 2 3 4 1
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='016.csv', mode='rt', encoding='utf-8', newline='')
_, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
print(tup)
arr1 = array('i', map(int, tup[0].split()))
print(arr1)

# 1
_index = arr1.index(max(arr1))
arr1[0], arr1[_index] = arr1[_index], arr1[0]
print(*arr1)

# 2
_index, _max = float('-inf'), float('-inf')
for i in range(len(arr1)):
    if arr1[i] > _max:
        _max = arr1[i]
        _index = i
arr1[0], arr1[_index] = arr1[_index], arr1[0]
print(*arr1)