'''
Больше 5

Найдите все элементы в массиве, которые больше 5, и замените их на 0, 
используя функцию numpy.where.

Вход: последовательность целых чисел, разделенных пробелом.

Выход: последовательность целых чисел, разделенных пробелом, соответствующая условию.

Sample Input:
7 8 18 18 6 5 12 10 14 10 13 15 0 7 11 13 14 1 3 2 7 21 32 27

Sample Output:
0 0 0 0 0 5 0 0 0 0 0 0 0 0 0 0 0 1 3 2 0 0 0 0
'''
import numpy as np
from sys import stdin
# stdin = open(file='127.csv', mode='rt', encoding='utf-8', newline='')

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
    # print(arr1)

    print(*np.where(5 < arr1, 0, arr1))