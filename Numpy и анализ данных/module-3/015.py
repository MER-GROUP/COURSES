'''
Вывод числа ПИ
На вход подается целое число n>0, cоздайте одномерный массив numpy, 
состоящий из n элементов, равных числу pi, и выведите его на экран.

Sample Input:
2
Sample Output:
[3.14159265 3.14159265]
'''
import numpy as np

print(np.full(shape=int(input()), fill_value=np.pi))

# print(*np.full((1, int(input())), np.pi))