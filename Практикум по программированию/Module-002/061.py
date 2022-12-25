'''
Сумма степеней

Входные данные
Вводится натуральное число N, которое не превосходит 30.

Выходные данные
Вычислите 1+2^1+2^2+2^3+…+2^N.

Sample Input:
3
Sample Output:
15
'''
from functools import reduce
from operator import add

n = int(input())

print(
    reduce(
        add,
        map(
            lambda x, y: x**y,
            (2 for _ in range(n)),
            range(1, n+1)
        ),
        1
    )
)

def sum_rec(n):
    if 0 == n:
        return 1
    else:
        return 2**n + sum_rec(n-1)

print(sum_rec(n))

s = 1
for i in range(1, n+1):
    s += 2**i

print(s)