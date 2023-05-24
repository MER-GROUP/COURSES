'''
Одномерный numpy массив 4
Создайте массив, содержащий 10 равноудаленных элементов в интервале от -5 до 5

Sample Input:

Sample Output:
[-5.         -3.88888889 -2.77777778 -1.66666667 -0.55555556  0.55555556
  1.66666667  2.77777778  3.88888889  5.        ]
'''
import numpy as np

print(np.linspace(-5, 5, 10, dtype=float))