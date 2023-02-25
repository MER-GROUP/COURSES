'''
Диаметр множества
Выведите диаметр данного множества – максимальное 
расстояние между любыми двумя точками.

Входные данные
Программа получает на вход набор точек на плоскости. 
Сначала задано количество точек n, затем идет последовательность 
из n строк, каждая из которых содержит два числа: координаты точки. 
Величина n не превосходит 100000, все исходные координаты – целые числа, 
не превосходящие 103.

Выходные данные
Необходимо вывести диаметр данного множества (действительное число 
с  точностью до 10 значащих цифр после запятой).

Sample Input:
2
1 2
2 3
Sample Output:
1.4142135623

PS:
Вычисление расстояния между взятыми на плоскости двумя точками А(х А; у А) и В(х В; у В), 
выполняется по формуле d = √((хА – хВ)2 + (уА – уВ)2), где d – длина отрезка, 
который соединяет эти точки на плоскости.

Здесь нужно найти максимальную величину d. 
Точность результата по аналогии с  задачей - центр цяжести.
'''
import sys  
from collections import namedtuple
coords = namedtuple('coords', ('x', 'y'))

def round_10(n: float) -> float:
    start, end = str(n).split('.')
    return float(start + '.' + end[:10])

def distance(a: coords, b: coords) -> float:
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5

# sys.stdin = open(file='041.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = map(str.strip, sys.stdin.read().splitlines())
# print(*arr, sep='\n') # test

arr = tuple(coords._make(map(int, el.split())) for el in arr)
# print(*arr) # test

max_n = float('-inf')
for a in arr:
    for b in arr:
        if a == b: continue
        buf = distance(a, b)
        if buf > max_n: max_n = buf
print(round_10(max_n))