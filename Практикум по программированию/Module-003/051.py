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

# sys.stdin = open(file='051.csv', mode='rt', encoding='utf-8', newline='')
_, *arr = map(str.strip, sys.stdin.read().splitlines())
# print(*arr, sep='\n') # test

## 1
print(len(set(map(int, ''.join(arr).split()))))

## 2
from collections import Counter
print(len(Counter(''.join(arr).split()).keys()))