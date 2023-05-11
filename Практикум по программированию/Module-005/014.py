'''
Двоичный поиск
Реализуйте алгоритм бинарного поиска.

Входные данные
В первой строке входных данных содержатся натуральные 
числа N и K (0 < N, K < 100000). Во второй строке задаются 
N элементов первого массива, отсортированного по возрастанию, 
а в третьей строке – K элементов второго массива. Элементы 
обоих массивов - целые числа, каждое из которых по модулю не 
превосходит 10^9

Выходные данные
Требуется для каждого из K чисел вывести в отдельную строку "YES", 
если это число встречается в первом массиве, и "NO" в противном случае.

Sample Input:
10 5
1 2 3 4 5 6 7 8 9 10
-2 0 4 9 12
Sample Output:
NO
NO
YES
YES
NO
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='014.csv', mode='rt', encoding='utf-8', newline='')
_, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
print(tup)
arr1 = array('i', sorted(map(int, tup[0].split())))
print(arr1)
arr2 = array('i', map(int, tup[1].split()))
print(arr2)

# 1
pass