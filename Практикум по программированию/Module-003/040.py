'''
Центр тяжести
Выведите координаты центра тяжести данного множества точек.

Входные данные
Программа получает на вход набор точек на плоскости. 
Сначала задано количество точек n, затем идет последовательность из n строк, 
каждая из которых содержит два числа: координаты точки. 
Величина n не превосходит 100, все исходные координаты – целые числа, 
не превосходящие 10^3.

Выходные данные
Выведите  координаты центра тяжести данного множества точек. 
Ответ - пара действительных чисел с пробелом между ними, 
необходимо выводить с точностью до 10 значащих цифр после запятой. 
При этом ответ не надо округлять, лишние цифры просто отбрасываются.

Sample Input:
2
1 2
2 3
Sample Output:
1.5 2.5
'''
import sys  
from collections import namedtuple
from statistics import mean

def round_10(n: float) -> float:
    start, end = str(n).split('.')
    return float(start + '.' + end[:10])

# sys.stdin = open(file='040.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = map(str.strip, sys.stdin.read().splitlines())
# print(*arr, sep='\n') # test

coords = namedtuple('coords', ('x', 'y'))
arr = (coords._make(map(int, el.split())) for el in arr)
# print(*arr) # test

x, y = zip(*arr)
x, y = float(mean(x)), float(mean(y))
# print(f'{x} {y}') # test
# print(f'{int(x * 1e10) / 1e10} {int(y * 1e10) / 1e10}') # or
print(f'{round_10(x)} {(round_10(y))}') # or