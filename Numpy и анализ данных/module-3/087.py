'''
greater_10

Напишите функцию greater_10(arr), которая принимает на вход одномерный массив 
и возвращает массив из элементов, которые больше 10.

Вызывать функцию не нужно, только создать.

Sample Input:
-8 -9 1 14 4 -9 14 14 -4 1 13 5 -2 -4 -9 1 -10 -3 -3 -5 8 13
Sample Output:
[14 14 14 13 13]
'''
import numpy as np

def greater_10(arr: np) -> np:
    return arr[arr > 10]

if __name__ == '__main__':
    print(
        greater_10(
            np.array(
                object='-8 -9 1 14 4 -9 14 14 -4 1 13 5 -2 -4 -9 1 -10 -3 -3 -5 8 13'.split(),
                dtype=int
            )
        )
    )