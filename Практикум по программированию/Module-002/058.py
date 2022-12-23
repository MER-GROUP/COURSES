'''
Геометрическая прогрессия
По данным натуральным числам a и n 
вычислите сумму 1+a^1+a^2+...+a^n, 
не используя формулу суммы геометрической прогрессии. 
Время работы программы должно быть пропорционально n.

Входные данные
Вводятся 2 числа - a и n.

Выходные данные
Необходимо вывести  значение суммы.

Sample Input:
2
2
Sample Output:
7
'''
from functools import reduce
from operator import add

a, n = (int(input()) for _ in range(2))
print(
    reduce(
        add,
        map(
            lambda a, n: a**n,
            [a for _ in range(n)],
            range(1, n+1)
        ),
        1
    )
)

s = 1
for x, y in zip([a for _ in range(n)] ,range(1, n+1)):
    s += x**y

print(s)

def geometric_progression(a, n):
    if 0 == n:
        return 1
    else:
        return a**n + geometric_progression(a, n-1)
        
print(geometric_progression(a, n))