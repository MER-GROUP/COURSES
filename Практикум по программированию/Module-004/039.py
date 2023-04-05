'''
Ферзи
Известно, что на доске 8×8 можно расставить 8 ферзей так, 
чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, 
определите, есть ли среди них пара бьющих друг друга.

Входные данные
Программа получает на вход восемь пар чисел, каждое число 
от 1 до 8 - координаты 8 ферзей.

Выходные данные
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

Sample Input 1:
1 7
2 4
3 2
4 8
5 6
6 1
7 3
8 5
Sample Output 1:
NO

Sample Input 2:
1 8
2 7
3 6
4 5
5 4
6 3
7 2
8 1
Sample Output 2:
YES
'''
import sys
from array import array
from copy import copy

sys.stdin = open(file='039.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
# arr = array('i', list(map(int, arr[0].split())))
print(arr) # test

pass