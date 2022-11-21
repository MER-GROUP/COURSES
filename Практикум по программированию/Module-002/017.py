'''
Автопробег
За день машина проезжает n километров. 
Сколько дней нужно, чтобы проехать маршрут длиной m километров?

При решении этой задачи нельзя пользоваться 
условной инструкцией if и циклами.

Входные данные
Программа получает на вход натуральные 
числа n и m, не превосходящие 10000.

Выходные данные
Выведите ответ на задачу.

Sample Input:
700
750
Sample Output:
2
'''
# from math import ceil
# n, m = int(input()), int(input())
# print(ceil(m / n))

# n, m = int(input()), int(input())
# print((m + n - 1) // n)

# n, m = int(input()), int(input())
# print(-(m // -n))

# n, m = int(input()), int(input())
# print(abs(m // -n))

a, b = int(input()), int(input())
print(b // a + (b % a > 0))