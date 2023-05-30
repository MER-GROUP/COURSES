'''
Массив numpy 1
На вход подаются 2 числа a и b. Создайте массив numpy, 
содержащий числа от a до b включительно, кратные 3, выведите его на экран.

Sample Input:
0 3
Sample Output:
[0 3]
'''
import numpy as np

a, b = map(int, input().split())
_arr = np.array(
    [i for i in range(a, b+1) if not i%3]
)
print(_arr)