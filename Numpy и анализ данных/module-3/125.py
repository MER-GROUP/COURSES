'''
Космическое танго на линии окружности

Даны два одномерных массива x и y, содержащие координаты точек на плоскости. 
Необходимо найти все точки, которые лежат на окружности с радиусом R = 5 и 
центром в точке (0, 0), а затем вычислить синус и косинус угла между вектором, 
соединяющим каждую из этих точек с центром окружности, и осью X. Считать, 
что точка лежит на окружности если расстояние от этой точки до центра 
окружности r: R - tol <= r <= R + tol, где tol - погрешность.

Вход: Первые две строки последовательности действительных чисел разделенных 
пробелами - массивы с координатами точек x и y. Третья строка: действительное число - tol.

Выход: Две строки действительных чисел, разделённых пробелом - косинус 
и синус соответствующих углов, округленные до трех знаков после запятой. 
Результат округляйте только в конце вычислений.

Sample Input:
5.1 0 -4.9 4.4
0.1 4.87 -0.1 4.2
.2

Sample Output:
1.0 0.0 -1.0
0.02 1.0 -0.02
'''
import numpy as np
from sys import stdin
# stdin = open(file='125.csv', mode='rt', encoding='utf-8', newline='')

if __name__ == '__main__':
#     arr = np.fromstring(
#         string=stdin.read(),
#         # dtype=int,
#         dtype=float,
#         sep = ' '
#     )
#     print(arr) # test #
#     print(type(arr)) # test #

    arr1, arr2, arr3, *_ = (np.fromstring(string=i, dtype=float, sep=' ') for i in stdin)
    # print(arr1, arr2, arr3, sep='\n')

    R = 5
    tol, *_ = arr3 

    hypot = np.hypot(arr1, arr2)
    # print(hypot) # test

    # mask_less_5 = (5 >= hypot)
    # print(mask_less_5) # test

    mask_less_5 = (R - tol <= hypot) & ((R + tol >= hypot))
    # print(mask_less_5) # test

    x = arr1[mask_less_5]
    # print(x) # test
    y = arr2[mask_less_5]
    # print(y) # test
    h = hypot[mask_less_5]
    # print(h) # test

    cos = x/h
    sin = y/h

    print(*cos.round(3))
    print(*sin.round(3))