'''
Делители числа
Выведите все натуральные делители числа x 
в порядке возрастания (включая 1 и само число).

Входные данные
Вводится натуральное число x

Выходные данные
Выведите все делители числа x

Sample Input:
32
Sample Output:
1 2 4 8 16 32
'''
n = int(input())
print(*(i for i in range(1, n+1) if not n % i))