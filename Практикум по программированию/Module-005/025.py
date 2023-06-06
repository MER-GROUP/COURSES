'''
Разные
Дано N чисел, требуется выяснить, сколько среди них различных.

Входные данные
В первой строке дано число N – количество чисел. (1 <= N <= 100000) 
Во второй строке даны через пробел N чисел, каждое не превышает 2*10^9 по модулю.

Выходные данные
Выведите число, равное количеству различных чисел среди данных.

Sample Input:
5
1 0 1 2 0
Sample Output:
3
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='025.csv', mode='rt', encoding='utf-8', newline='')
_, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
print(tup)
arr = array('i', map(int, tup[0].split()))
print(arr)