'''
multpl

Написать функцию multpl(arr1, arr2), которая на вход принимает два одномерных 
numpy массива arr1 и arr2 и возвращает новый массив, содержащий результат их 
поэлементного сложения. Функцию вызывать не нужно, просто создайте ее.

Sample Input:
86 84 83 76 72 69 71 99
86 84 83 76 72 69 71 99
Sample Output:
[172 168 166 152 144 138 142 198]
'''
import numpy as np

def multpl(arr1: np, arr2: np) -> np:
    return arr1 + arr2

if __name__ == '__main__':
    print(
        multpl(
            np.array('86 84 83 76 72 69 71 99'.split(), dtype=int), 
            np.array('86 84 83 76 72 69 71 99'.split(), dtype=int)
        )
    )