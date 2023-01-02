'''
Список квадратов
Выведите все точные квадраты натуральных чисел, 
не превосходящие данного числа N.

Входные данные
Задано единственное целое число N

Выходные данные
Необходимо вывести  все точные квадраты натуральных чисел, 
не превосходящие данного числа N.

Sample Input:
15
Sample Output:
1
4
9
'''
n = int(input())
i = 1
while i**2 <= n:
    print(i**2)
    i += 1

# print(*[i**2 for i in range(1, n+1) if i**2 <= n], sep='\n')