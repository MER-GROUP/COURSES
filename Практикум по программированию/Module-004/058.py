'''
Количество дней от начала эры
Требуется посчитать количество дней от начала эры до данного дня включительно. 
Началом эры считается первое января первого года.

Входные данные
В единственной строке входного файла находится дата в формате ДДММГГГГ.

Выходные данные
Выведите искомое количество дней.

Sample Input:
02010001
Sample Output:
2
'''
import sys
# from array import array
# from copy import copy

sys.stdin = open(file='058.csv', mode='rt', encoding='utf-8', newline='')
nm, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
print(nm)
# print(tup)
# arr = array('i', list(map(int, arr.split())))
# n, *m = map(int, nm.split())
# print(n)
# # arr = [list(map(int, tup[i].split())) for i in range(n)]
# arr = [[0]*n for _ in range(n)]
# [print(*i, sep='') for i in arr]

pass