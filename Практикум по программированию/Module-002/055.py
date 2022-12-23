'''
Факториал
Вычислите N! ("эн-факториал") – произведение всех 
натуральных чисел от 1 до N ( N!=1∙2∙3∙…∙ N ).

Входные данные
Вводится единственное число N – натуральное, не превосходит 12.

Выходные данные
Выведите полученное значение N!

Sample Input:
5
Sample Output:
120
'''
from functools import reduce
from operator import mul

n = int(input())
print(
    reduce(
        mul,
        range(2, n+1),
        1
    )
)

f = 1
for i in range(2, n+1):
    f *= i
print(f)

from math import factorial
print(factorial(n))