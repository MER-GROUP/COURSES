'''

'''
import numpy as np
from sys import stdin
stdin = open(file='120.csv', mode='rt', encoding='utf-8', newline='')

if __name__ == '__main__':
    # arr = np.fromstring(
    #     string=stdin.read(),
    #     dtype=float,
    #     sep = ' '
    # )
    # print(arr) # test #
    # print(type(arr)) # test #

    arr1, arr2 = (np.fromstring(string=i, dtype=float, sep=' ') for i in stdin)
    print(arr1, arr2, sep='\n')

    pass