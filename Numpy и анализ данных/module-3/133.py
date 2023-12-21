'''
3 без остатка

На вход поступает массив чисел в виде строки целых чисел, разделенных пробелом. 
Создайте новый массив, содержащий все элементы из исходного массива, кроме тех, 
которые делятся на 3 без остатка. Выведите этот массив на экран в виде строки чисел, 
разделенных пробелом. Если таких чисел нет, ничего выводить не нужно.

Sample Input:
1 2 3 4 5 6

Sample Output:
1 2 4 5
'''
import numpy as np
from sys import stdin
# stdin = open(file='133.csv', mode='rt', encoding='utf-8', newline='')

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
    # print(arr1) # test

    print(*arr1[np.where(arr1%3)])