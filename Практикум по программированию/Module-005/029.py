'''
Сортировка подсчетом

Реализуйте алгоритм сортировки подсчетом для произвольных чисел, 
по модулю не превосходящих 10000.

Входные данные

На вход программе сначала подается значение n ≤ 100000 – количество 
элементов в массиве. В следующей строке входных данных расположены 
сами элементы массива – целые числа, по модулю не превосходящие 10000.

Выходные данные

Распечатайте отсортированный по неубыванию массив.

Sample Input:
5
1 3 4 2 5

Sample Output:
1 2 3 4 5
'''
import sys
from array import array
# from copy import copy

if __name__ == '__main__':
    sys.stdin = open(file='029.csv', mode='rt', encoding='utf-8', newline='')
    n, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
    print(n)
    print(tup)
    arr = array('i', map(int, tup[0].split()))
    print(arr)