'''
Число сочетаний
По данным натуральным n и k вычислите значение C^k_n = n!/(k!*(n-k)!)

(число сочетаний из n элементов по k).

Входные данные
Вводятся 2 числа - n и k (n > k; n, k <= 30 ).

Выходные данные
Необходимо вывести значение C^k_n

Sample Input:
2
1
Sample Output:
2
'''
from math import factorial

n, k = (int(input()) for _ in range(2))
res = int(factorial(n)/(factorial(k) * factorial(n - k)))
print(res)