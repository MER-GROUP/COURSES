'''
Минимальная и максимальная цифры

Входные данные
Задано единственное число N, не больше 1000.

Выходные данные
Необходимо вывести наименьшую и наибольшую цифры данного числа через пробел.

Sample Input:
37
Sample Output:
3 7
'''
import sys

# sys.stdin = open(file='105.csv', mode='rt', encoding='utf-8', newline='')
tup = sys.stdin.read()

print(min(tup, key=int), max(tup, key=int))

# min_n = float('infinity')
# max_n = float('-infinity')
# for i in tup:
#     if int(i) > max_n: max_n = int(i)
#     if int(i) < min_n: min_n = int(i)
# print(min_n, max_n)