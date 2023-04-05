'''
Большой сдвиг
Дан список из N (1≤N≤100000) целых чисел и число K (|K|<100000). 
Циклически сдвиньте список на |K| элементов вправо, 
если K – положительное и влево, если отрицательное число.

Входные данные
Программа получает на вход список целых чисел, затем число K.

Выходные данные
Выведите ответ на задачу.

Примечание
Решение должно иметь сложность O(N), то есть не должно зависеть от K. 
Дополнительным списком пользоваться нельзя.

Sample Input:
5 3 7 4 6
3
Sample Output:
7 4 6 5 3
'''
import sys
from array import array
from copy import copy

sys.stdin = open(file='040.csv', mode='rt', encoding='utf-8', newline='')
arr, n = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr.split())))
n = int(n)
print(arr) # test
print(n) # test

pass