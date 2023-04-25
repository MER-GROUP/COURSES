'''
Юлианский календарь
По заданному числу n от 1 до 365 определите, на какое число какого месяца 
приходится день невисокосного года с номером n.

Входные данные
Дано одно целое число n.

Выходные данные
Программа должна вывести два числа: число месяца (от 1 до 31) 
и номер месяца (от 1 до 12), соответствующие  дню  с номером n.

Sample Input:
90
Sample Output:
31 3
'''
import sys
# from array import array
# from copy import copy

sys.stdin = open(file='056.csv', mode='rt', encoding='utf-8', newline='')
nm, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(nm)
# print(tup)
# arr = array('i', list(map(int, arr.split())))
n, *m = map(int, nm.split())
print(n)
# # arr = [list(map(int, tup[i].split())) for i in range(n)]
# arr = [[0]*n for _ in range(n)]
# [print(*i, sep='') for i in arr]

pass