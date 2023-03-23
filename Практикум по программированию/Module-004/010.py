'''
Максимум в массиве
Вводится массив, состоящий из целых чисел. Найти наибольшее среди них.

Входные данные
Сначала задано число N — количество элементов в массиве (1 ≤ N ≤ 35). 
Далее через пробел записаны N чисел — элементы массива. Массив состоит из целых чисел.

Выходные данные
Необходимо вывести значение наибольшего элемента в массиве.

Sample Input:
3
1 2 3
Sample Output:
3
'''
import sys
from array import array

# sys.stdin = open(file='010.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

# print(max(arr)) # 1

_max = float('-inf') # 2
for _el in arr:
    _max = max(_max, _el)
print(_max)

# input()
# print(
#     __import__('functools').reduce(
#         lambda a, b: (a >= b) * a + (a < b) * b, [int(i) for i in input().split()]
#     )
# )