'''
Пузырьковая сортировка: количество обменов
Ввод и вывод данных производятся через стандартные потоки ввода-вывода.

Определите, сколько обменов сделает алгоритм пузырьковой сортировки 
по возрастанию для данного массива.

Входные данные
На первой строке дано число N (1 ≤ N ≤ 1000) – количество элементов 
в массиве. На второй строке – сам массив. Гарантируется, что все 
элементы массива различны и не превышают по модулю 10^9.

Выходные данные
Выведите одно число – количество обменов пузырьковой сортировки.

Sample Input:
5
1 2 3 4 5
Sample Output:
0
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='021.csv', mode='rt', encoding='utf-8', newline='')
_, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
print(tup)
arr1 = array('i', map(int, tup[0].split()))
print(arr1)

# 1
pass