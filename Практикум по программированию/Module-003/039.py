'''
Наиболее удаленная точка
Выведите координаты наиболее удаленной от начала координат точки.

Входные данные
Программа получает на вход набор точек на плоскости. 
Сначала задано количество точек n, затем идет последовательность из n строк, 
каждая из которых содержит два числа: координаты точки. 
Величина n не превосходит 100, все исходные координаты – целые числа, 
не превосходящие 10^3 по абсолютной величине.

Выходные данные
Выведите  координаты точки, наиболее удаленной от начала координат.

Sample Input:
2
1 2
2 3
Sample Output:
2 3
'''
import sys  
from collections import namedtuple
from math import hypot

# sys.stdin = open(file='039.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = map(str.strip, sys.stdin.read().splitlines())
# print(*arr, sep='\n') # test

coordinate = namedtuple('coordinate', ('x', 'y'))
# coordinates = (coordinate(*map(int, el.split())) for el in arr) # or
coordinates = (coordinate._make(map(int, el.split())) for el in arr) # or
# print(*coordinates, sep='\n') # test
# print(type(coordinates)) # test

print(
    *max(
        coordinates,
        # key=lambda x: hypot(*x) # or
        key=lambda c: hypot(c.x, c.y) # or
    )
)