'''
Приближенный двоичный поиск
Реализуйте алгоритм приближенного бинарного поиска.

Входные данные
В первой строке входных данных содержатся числа N и K (0 < N, K  < 100001). 
Во второй строке задаются N чисел первого массива, отсортированного по неубыванию, 
а в третьей строке – K чисел второго массива. Каждое число в обоих массивах 
по модулю не превосходит 2*10^9.

Выходные данные
Для каждого из K чисел выведите в отдельную строку число из первого массива, 
наиболее близкое к данному. Если таких несколько, выведите меньшее из них.

Sample Input:
5 5
1 3 5 7 9
2 4 8 1 6
Sample Output:
1
3
7
1
5
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='012.csv', mode='rt', encoding='utf-8', newline='')
_, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
print(_)
print(tup)
arr1 = array('i', map(int, tup[0].split()))
print(arr1)
arr2 = array('i', map(int, tup[1].split()))
print(arr2)

pass