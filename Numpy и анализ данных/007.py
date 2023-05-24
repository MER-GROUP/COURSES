'''
Одномерный numpy массив 5
Создайте массив, содержащий числа от 10 до 1 в обратном порядке.

Sample Input:

Sample Output:
[10  9  8  7  6  5  4  3  2  1]
'''
import numpy as np

print(np.arange(10, 0, -1, dtype=int))