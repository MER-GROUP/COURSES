'''
Тип float16
На вход подается  строка действительных чисел разделенных пробелом. 
Напишите программу, которая создает одномерный массив из чисел, 
введенной строки с типом float16. Выведите на экран данный массив 
его тип и размер в байтах каждого элемента массива.

Sample Input:
3.4 6 4.333
Sample Output:
[3.4   6.    4.332]
float16 2
'''
import numpy as np

if __name__ == '__main__':
    arr = np.array(input().split(), dtype=np.float16)
    print(arr)
    print(arr.dtype, arr.itemsize)