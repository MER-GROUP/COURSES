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

def sorted_sides(a: coords, b: coords, c: coords) -> bool:
    pass

def is_triangle(a: coords, b: coords, c: coords) -> bool:
    # sides of triangle
    ab, bc, ca = sorted(
        (
            hypot(a.x - b.x, a.y - b.y),
            hypot(b.x - c.x, b.y - c.y),
            hypot(c.x - a.x, c.y - a.y)
        )
    )
    return (True, False)[ca > ab + bc]

def is_all_on_same_line(a: coords, b: coords, c: coords) -> bool:
    return (False, True)[a.x == b.x == c.x or a.y == b.y == c.y]

def heron(a: coords, b: coords, c: coords) -> float:
    # sides of triangle
    ab, bc, ca = sorted(
        (
            hypot(a.x - b.x, a.y - b.y),
            hypot(b.x - c.x, b.y - c.y),
            hypot(c.x - a.x, c.y - a.y)
        )
    )
    p = (ab + bc + ca) / 2
    return (p * (p - ab) * (p - bc) * (p - ca))**0.5

sys.stdin = open(file='044.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = map(str.strip, sys.stdin.read().splitlines())
# print(*arr, sep='\n') # test

arr = tuple(coords._make(map(int, el.split())) for el in arr)
# print(*arr) # test

s_max = float('-inf')
for i in range(len(arr)-2):
    for j in range(i+1, len(arr)-1):
        for k in range(j+1, len(arr)):
            # coordinates of the triangle
            a, b, c = arr[i], arr[j], arr[k]
            # if triangle exists and not all sides are on same line
            if is_triangle(a, b, c) and not is_all_on_same_line(a, b, c):
                s_max = max(heron(a, b, c), s_max)
print(round(s_max, 1))