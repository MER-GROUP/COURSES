'''
Сложное уравнение
Решить в целых числах уравнение ( ax + b ) : ( cx + d ) = 0.

Входные данные
Вводятся 4 числа: a, b, c и d; c и d не равны нулю одновременно.

Выходные данные
Необходимо вывести все целочисленные решения, 
если их число конечно, “NO” (без кавычек), 
если целочисленных решений нет, и “INF” (без кавычек), 
если их бесконечно много.

Sample Input:
1
1
2
2
Sample Output:
NO
'''

"""
Алгоритм

( ax + b ) : ( cx + d ) = 0

Сводим уравнение к системе:

{ ax + b = 0
{ cx + d ≠ 0

{ ax = -b
{ cx ≠ -d
"""
a, b, c, d = (int(input()) for _ in range(4))
if 0 == a == b:
    print('INF')
elif 0 == a or (b * c == a * d):
    print('NO')
elif 0 != a and (-b / a == int(-b / a)):
    print(int(-b / a))
else:
    print('NO')

# if a == 0 and b == 0:
#     print('INF')
# elif a == 0 or b * c == a * d:
#     print('NO')
# elif b % a == 0:
#     x = -b // a
#     print(x)
# else:
#     print('NO')