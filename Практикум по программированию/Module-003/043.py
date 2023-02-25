'''
Максимальный периметр
Среди исходных точек найдите три, образующие треугольник с максимальным периметром. 
Выведите данный периметр.

Входные данные
Программа получает на вход набор точек на плоскости. 
Сначала задано количество точек n (2 < n < 101), 
затем идет последовательность из n строк, каждая из которых содержит два числа: 
координаты точки. Все исходные координаты – целые числа, не превосходящие 10^3.

Выходные данные
Необходимо вывести найденный периметр в виде действительного числа 
с точностью до 12 значащих цифр после запятой.

Sample Input:
4
0 0
0 1
1 0
1 1
Sample Output:
3.414213562373

Sample Input:
4
3 7
2 5
11 9
33 34
Sample Output:
Правильный ответ: 85.600479966071
Ответ вашего решения:  75.255308921876

PS:
Вычисление расстояния между взятыми на плоскости двумя точками А(х А; у А) и В(х В; у В), 
выполняется по формуле d = √((хА – хВ)2 + (уА – уВ)2), где d – длина отрезка, 
который соединяет эти точки на плоскости.
'''
import sys  
from collections import namedtuple
coords = namedtuple('coords', ('x', 'y'))
from math import hypot

def round_10(n: float) -> float:
    start, end = str(n).split('.')
    return float(start + '.' + end[:12])

# def distance(a: coords, b: coords) -> float:
#     return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5

# sys.stdin = open(file='043.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = map(str.strip, sys.stdin.read().splitlines())
# print(*arr, sep='\n') # test

arr = tuple(coords._make(map(int, el.split())) for el in arr)
# print(*arr) # test

perimetr_max = float('-inf')
for a in arr:
    for b in arr:
        for c in arr:
            if a == b == c: continue
            ab, bc, ca = sorted(
                (
                    # distance(a, b),
                    # distance(b, c),
                    # distance(c, a)
                    hypot(a.x - b.x, a.y - b.y),
                    hypot(b.x - c.x, b.y - c.y),
                    hypot(c.x - a.x, c.y - a.y)
                )
            )
            # print(ab, bc, ca) # test
            if not ca > ab + bc:
                perimetr_max = max(perimetr_max, sum((ab, bc, ca)))
            # print(perimetr_max) # test
print(round_10(perimetr_max))