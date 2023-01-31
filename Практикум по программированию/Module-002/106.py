'''
Двоичная запись
Дано натуральное число N. Выведите его представление 
в двоичном виде в обратном порядке.

Входные данные
Задано единственное число N

Выходные данные
Необходимо вывести требуемое представление числа N.

Sample Input:
6
Sample Output:
011
'''
import sys

# sys.stdin = open(file='106.csv', mode='rt', encoding='utf-8', newline='')
tup = sys.stdin.read()

print(bin(int(tup))[2:][::-1])

# ans = str()
# N = int(tup)
# while N: 
#     ans += str(N%2)
#     N = N//2
# print(ans)

# n = int(tup)
# s = str()
# while n > 0:
#     s = str(n%2) + s
#     n = n // 2
# print(s[::-1])