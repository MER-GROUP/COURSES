'''
Пирамидальная сортировка
Отсортируйте данный массив. Используйте пирамидальную сортировку.

Входные данные
Первая строка входных данных содержит количество элементов 
в массиве N,  N  ≤  105. Далее задаются N целых чисел, 
не превосходящих по абсолютной величине 109.

Выходные данные
Выведите эти числа в порядке неубывания.

Sample Input:
5
5 4 3 2 1
Sample Output:
1 2 3 4 5
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='026.csv', mode='rt', encoding='utf-8', newline='')
_, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
print(tup)
arr = array('i', map(int, tup[0].split()))
print(arr)

pass