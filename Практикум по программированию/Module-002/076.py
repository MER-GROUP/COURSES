'''
Количество решений

Входные данные
Вводятся 5 чисел: a, b, c, d и e.

Выходные данные
Найдите все целые решения уравнения 
( ax^3 + bx^2 + cx + d ) / ( x - e ) = 0 на отрезке [0,1000] 
и выведите их количество.

Sample Input:
1
2
3
4
5
Sample Output:
0
'''
a, b, c, d, e = (int(input()) for _ in range(5))
count = 0
for x in range(1001):
    try:
        if 0 == (a*x**3 + b*x**2 + c*x + d) / (x - e):
            count += 1
    except ZeroDivisionError:
        pass
print(count)