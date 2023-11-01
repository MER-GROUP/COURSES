'''
Коэффициент сопротивления воздуха

Найти коэффициент сопротивления воздуха
'''
import numpy as np
from sys import stdin
stdin = open(file='111.csv', mode='rt', encoding='utf-8', newline='')

if __name__ == '__main__':
    arr = np.fromstring(
        string=stdin.read(),
        dtype=float,
        sep = ' '
    )
    # print(arr) # test #
    # print(type(arr)) # test #

    rho = 1.225
    A = 2.28
    k = 0.15
    h = 0.01
    CD0 = 0.23
    DragCoef = (rho * A )/2 * (CD0 + k * np.sin(arr) + h * np.cos(arr))
    print(*DragCoef.round(3))