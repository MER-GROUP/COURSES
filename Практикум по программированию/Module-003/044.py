'''
Максимальная площадь
Среди исходных точек найдите три, образующие треугольник максимальной площади. 
Выведите данную площадь.

Входные данные
Программа получает на вход набор точек на плоскости. 
Сначала задано количество точек n (2 < n < 101), 
затем идет последовательность из n строк, каждая из которых содержит два числа: 
координаты точки. Все исходные координаты – целые числа, не превосходящие 10^3.

Выходные данные
Необходимо вывести найденную площадь в виде действительного числа.

Sample Input:
4
0 0
0 1
1 0
1 1
Sample Output:
0.5
'''
import sys  
from collections import namedtuple
coords = namedtuple('coords', ('x', 'y'))
from math import hypot

def round_10(n: float) -> float:
    start, end = str(n).split('.')
    return float(start + '.' + end[:12])

sys.stdin = open(file='044.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = map(str.strip, sys.stdin.read().splitlines())
# print(*arr, sep='\n') # test

arr = tuple(coords._make(map(int, el.split())) for el in arr)
print(*arr) # test

pass