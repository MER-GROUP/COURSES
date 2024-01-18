'''

'''
import numpy as np
from sys import stdin
stdin = open(file='142.csv', mode='rt', encoding='utf-8', newline='')

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
    arr1, arr2, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    # arr1, arr2, *_ = (np.array(i.split(), dtype=int) for i in stdin)
    # arr1, *_ = (np.fromstring(string=i, dtype=int, sep=' ') for i in stdin)
    print(arr1) # test
    print(arr2) # test

    pass