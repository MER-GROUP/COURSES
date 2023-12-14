'''
Больше 10 и меньше 20

На вход поступает массив в виде строки целых чисел, разделенных пробелом. 
Создайте новый массив, содержащий элементы из исходного массива, 
которые больше 10 и меньше 20. Используйте функцию numpy.where.

Sample Input:
12 21 18 0 9 10 5 2 7 18 3 13 16 4 0 5 11 16 2 17 16 18 21 0

Sample Output:
12 18 18 13 16 11 16 17 16 18
'''
import numpy as np
from sys import stdin
stdin = open(file='131.csv', mode='rt', encoding='utf-8', newline='')

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