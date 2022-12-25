'''
Сумма факториалов
1/0!+1/1!+1/2!+...

По данному натуральному числу N найдите сумму чисел 1+1/1!+1/2!+1/3!+...+1/N!. 
Количество действий должно быть пропорционально N.

Входные данные
Задано единственное число N (N<=5000).

Выходные данные
Необходимо вывести  результат вычисления в 
виде действительного числа c точностью до 5 знаков после запятой.

Sample Input:
1
Sample Output:
2.0
'''
from functools import reduce
from operator import add
from math import factorial as f

n = int(input())

print(
    round(
        reduce(
            add,
            map(
                lambda x, y: x/f(y),
                (1 for _ in range(n)),
                range(1, n+1)
            ),
            1
        ),
        5
    )
)

def sum_rec(n):
    if 0 == n:
        return 1
    else:
        return 1/f(n) + sum_rec(n-1)

print(sum_rec(n))

s = 1
for i in range(1, n+1):
    s += 1/f(i)

print(s)