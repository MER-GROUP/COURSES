'''
Побочная диагональ
Дано число n, n ≤ 100 . Создайте массив n×n и заполните его по следующему правилу:
- числа на диагонали, идущей из правого верхнего в левый нижний угол, равны 1; 
- числа, стоящие выше этой диагонали, равны 0;
- числа, стоящие ниже этой диагонали, равны 2.

Входные данные
Программа получает на вход число n.

Выходные данные
Необходимо вывести полученный массив. Числа разделяйте одним пробелом.

Sample Input:
4
Sample Output:
0 0 0 1
0 0 1 2
0 1 2 2
1 2 2 2
'''
import sys
# from array import array
# from copy import copy

sys.stdin = open(file='041.csv', mode='rt', encoding='utf-8', newline='')
n, *_ = tuple(map(str.strip, sys.stdin.read().splitlines()))
# arr = array('i', list(map(int, arr.split())))
n = int(n)
print(n) # test
arr = list()

pass