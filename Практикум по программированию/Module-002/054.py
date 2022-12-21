'''
Сумма квадратов
По данному натуральному n вычислите сумму 1^2+2^2+...+n^2.

Входные данные
Вводится единственное натуральное число n, не превосходящее 100

Выходные данные
Необходимо вывести  вычисленную сумму.

Sample Input:
2
Sample Output:
5
'''
from functools import reduce
from operator import add

n = int(input())
print(
    reduce(
        add,
        map(
            lambda x, y: x**y,
            range(1, n+1),
            [2 for _ in range(n)]
        ),
        0
    )
)

# print(
#     sum(
#         i**2 for i in range(1, n+1)
#     )
# )

# print(sum([i*i for i in range(int(input())+1)]))