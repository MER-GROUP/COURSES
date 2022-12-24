'''
Сумма - 2
По данному числу n вычислите сумму 4*(1-1/3+1/5-1/7+...+(-1)^n/(2n+1)).

Входные данные
Вводится одно число n, не превосходящее 100000.

Выходные данные
Необходимо вывести значение выражения, округляя до 5 знаков после запятой.

Sample Input:
1
Sample Output:
2.66667
'''
from functools import reduce
from operator import add

n = int(input())

print(
    round(
        4 * reduce(
            add,
            map(
                lambda x, y: x/y,
                ((1, -1)[i % 2] for i in range(1, n+1)),
                (2*i+1 for i in range(1, n+1))
            ),
            1
        ),
        5
    )
)

s = 1
m = -1
for i in range(1, n+1):
    s += m/(2*i+1)
    m *= -1

print(round(4*s, 5))

def sum_rec(n):
    if 0 == n:
        return 1
    else:
        return (-1)**n / (2 * n + 1) + sum_rec(n-1)

print(round(4*sum_rec(n), 5))