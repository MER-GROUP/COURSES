'''
Нечетные числа

Создайте массив, содержащий только нечетные числа от 1 до 50, используйте функцию numpy.where. 
Массив выведите в виде строки чисел, 
разделенных пробелом.
'''
import numpy as np
from sys import stdin
stdin = open(file='128.csv', mode='rt', encoding='utf-8', newline='')

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

    # arr1, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    # print(arr1)

    arr1 = np.arange(1, 51)
    print(*arr1[np.where(arr1 % 2)])

    # print(~np.arange(1, 50))

    # arr = np.where(np.arange(50) % 2 != 0)
    # arr = np.where(np.arange(50) % 2)
    # arr = np.where(np.arange(50))

    # arr = np.where(np.arange(40, 50))
    # print(arr)
    # # print()
    # print(np.where(arr))
    
    # arr = np.arange(50)
    # print(arr)
    # print()
    # print(np.where(arr % 2))