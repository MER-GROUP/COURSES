'''
Индексы всех отрицательных элементов

На вход подается строка чисел, разделенных пробелом, на ее основе создайте массив numpy. 
Найдите индексы всех отрицательных элементов в массиве и выведите их в виде массива numpy.

Sample Input:
2 -6 -10 -7 0 -6 3 7 8 10 -11 -11

Sample Output:
[ 1  2  3  5 10 11]
'''
import numpy as np
from sys import stdin
stdin = open(file='129.csv', mode='rt', encoding='utf-8', newline='')

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

    arr1, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    print(arr1)