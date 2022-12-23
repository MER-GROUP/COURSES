'''
Степень
Напишите программу, вычисляющую 2^N.

Входные данные
Вводится целое неотрицательное число N, которое не превосходит 30.

Выходные данные
Выведите число 2^N.

Sample Input:
3
Sample Output:
8
'''
from functools import reduce
from operator import mul

n = int(input())
print(
    reduce(
        mul,
        [2 for i in range(1, n+1) if 0 < i],
        1
    )
)

print(2**n)