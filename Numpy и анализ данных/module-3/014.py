'''
N единиц
На вход подается целое число n>0, cоздайте одномерный массив, 
состоящий из n единиц, и выведите его на экран.

Sample Input:
2
Sample Output:
[1. 1.]
'''
import numpy as np


print(np.ones(int(input()), dtype=float))