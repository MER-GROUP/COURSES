#!/usr/bin/env python
'''
Гистограмма

Рассчитать гистограмму распределения количества пассажиров на рейсах авиакомпании 
на основе данных, представленных в виде одномерного массива, поступающего 
в первой входной строке, во второй строке поступает целое 
число n - количество интервалов разбиения гистограммы. 
Вывести в первой строке частоты через пробел, во второй строке границы, 
получившихся интервалов, округленные до одного знака после запятой.

Sample Input:
125 195 189 147 133 124 190 97 159 120 174 125 112 93 170 120 191 120 165 166 154 181 167 158 159 128 182 151 190 131 96 175 117 103 181 156 131 93 171 101 120 118 142 156 172 88 125 100 183 159 176
4

Sample Output:
9 14 13 15
88.0 114.8 141.5 168.2 195.0
'''
import numpy as np
from sys import stdin
stdin = open(file='145.csv', mode='rt', encoding='utf-8', newline='')

if __name__ == '__main__':
#     arr = np.fromstring(
#         string=stdin.read(),
#         # dtype=int,
#         dtype=float,
#         sep = ' '
#     )
#     print(arr) # test #
#     print(type(arr)) # test #

    # arr1, arr2, arr3, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    # print(arr1, arr2, arr3, sep='\n')

    # arr1, arr2, *_ = (np.array(object=i.split(), dtype=str) for i in stdin)
    # arr1, arr2, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    # arr1, arr2, *_ = (np.array(i.split(), dtype=int) for i in stdin)
    # arr1, *_ = (np.fromstring(string=i, dtype=float, sep=' ') for i in stdin)
    arr1, arr2, *_ = (np.fromstring(string=i, dtype=float, sep=' ') for i in stdin)
    print(arr1) # test
    print(arr2) # test

    pass