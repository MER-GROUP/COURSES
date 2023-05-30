'''
Фибоначчи
На вход подается целое число n>1. Создайте numpy массив, 
содержащий n первых чисел Фибоначчи, выведите его на экран.

Sample Input:
2
Sample Output:
[0 1]
'''
import numpy as np

def fibo(n: int) -> int:
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

print(np.array([fibo(i) for i in range(int(input()))]))