'''
На вход программе на первой строке подаются коэффициенты многочлена, 
разделенные символом пробела и целое число x на второй строке. 
Напишите программу, которая вычисляет значение указанного многочлена при заданном значении x.
'''
'''
Первый тест задает многочлен 2x^2+4x+3
Sample Input 1:
2 4 3
10
2*10^2 + 4*10^1 + 3
Sample Output 1:
243
'''
# Решение
from functools import reduce
from operator import add

def evaluate(coefficients, x):
    return reduce(
        add,
        map(
            lambda a, x, n: a * x**n,
            coefficients[ : -1], 
            [x] * (len(coefficients) - 1), 
            [i for i in range(len(coefficients)-1, 0, -1)]
        ),
        coefficients[-1]
    )

print(evaluate(list(map(int, input().split())), int(input())))