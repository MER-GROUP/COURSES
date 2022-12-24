'''
Сумма - 1
По данному числу n вычислите сумму 1+1/2^2+1/3^2+...+1/n^2.

Входные данные
Вводится одно число n, не превосходящее 100000.

Выходные данные
Необходимо вывести значение суммы, округляя до 5 знаков после запятой.

Sample Input:
2
Sample Output:
1.25
'''
from functools import reduce
from operator import add

n = int(input())

print(
    round(
        reduce(
            add,
            map(
                lambda x: 1/(x**2),
                range(2, n+1)
            ),
            1
        ),
        5
    )
)

def sum_rec(n):
    if 1 == n:
        return 1
    else:
        return 1/(n**2) + sum_rec(n-1)

print(round(sum_rec(n), 5))

s = 1
for i in range(2, n+1):
    s += 1/(i**2)

print(round(s, 5))

print(
    round(sum([1/(i**2) for i in range(2, n+1)], 1), 5)
)

print(
    round(sum([1/(i**2) for i in range(1, n+1)]), 5)
)