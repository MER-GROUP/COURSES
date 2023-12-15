'''
Больше 50

На вход поступает массив целых чисел в виде строки. Найдите первый элемент в массиве, 
который больше 50 и выведите его на экран, используйте функцию numpy.where. 
Если такого элемента нет, ничего выводить не нужно.

Sample Input:
11 16 43 11 36 58 55 31 64 12 40 46 55 54 53 62 13 50 18 65 18 15 64 33

Sample Output:
58
'''
import numpy as np
from sys import stdin
stdin = open(file='132.csv', mode='rt', encoding='utf-8', newline='')

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

    arr1, *_ = (np.fromstring(string=i, dtype=float, sep=' ') for i in stdin)
    print(arr1)