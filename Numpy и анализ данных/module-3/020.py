'''
Функция convert_type
Напишите функцию convert_type(), которая принимает на вход 
одномерный numpy массив и возвращает новый массив того же 
размера, но с типом данных str.

Нужно только определить функцию, вызывать ее не нужно!

Sample Input:
2 3.3 5 5
Sample Output:
['2.0' '3.3' '5.0' '5.0']
'''
import numpy as np

def convert_type(arr: np) -> np:
    return arr.astype(dtype=str)

if __name__ == '__main__':
    print(convert_type(np.array(input().split())))