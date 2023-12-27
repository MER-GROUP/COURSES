'''
Работа с данными о клиентах

На вход в первой строке поступает массив с данными о клиентах, 
в котором каждый элемент представляет собой возраст клиента. 
Во второй строке поступают два целых числа, разделенных пробелом: 
min и max. Найдите все значения, которые выходят за диапазон (min, max), 
и замените их на среднее значение возраста. Выведите итоговый массив 
в строчку через пробел. Результат округляйте до одного знака после запятой.

Sample Input:
55 54 7 75 37 38 91 37 44 31
15 65

Sample Output:
55.0 54.0 46.9 46.9 37.0 38.0 46.9 37.0 44.0 31.0
'''
import numpy as np
from sys import stdin
stdin = open(file='137.csv', mode='rt', encoding='utf-8', newline='')

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

    arr1, arr2, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    # arr1, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    print(arr1) # test
    print(arr2) # test

    pass