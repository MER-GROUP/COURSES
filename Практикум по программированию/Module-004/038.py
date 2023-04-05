'''
Кегельбан
N кеглей выставили в один ряд, занумеровав их слева направо числами 
от 1 до N. Затем по этому ряду бросили K шаров, при этом i-й шар 
сбил все кегли с номерами от l_i до r_ir включительно. Определите, 
какие кегли остались стоять на месте.

Входные данные
Программа получает на вход количество кеглей N и количество бросков K. 
Далее идет K пар чисел l_i, r_i, при этом 1≤l_i≤r_i≤N.

Выходные данные
Программа должна вывести последовательность из N символов, 
где j-й символ есть “I”, если j-я кегля осталась стоять, или “.”, 
если j-я кегля была сбита.

Sample Input:
10 3
8 10
2 5
3 6
Sample Output:
I.....I...
'''
import sys
# from array import array
# from copy import copy

# sys.stdin = open(file='038.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
# arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

_len_bowling, _ = map(int, arr[0].split())
_arr_bowling = ['I'] * _len_bowling
# print(*_arr_bowling, sep='') # test

for _str in arr[1:]:
    _left, _right = map(int, _str.split())
    for _i in range(_left-1, _right):
        _arr_bowling[_i] = '.'
print(*_arr_bowling, sep='')