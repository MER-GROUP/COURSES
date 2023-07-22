'''
func1

Напишите функцию func1(a, b), которая принимает два одномерных массива a и b и возвращает 
новый массив, в котором на каждой позиции i находится результат операции a[i] > b[i] & a[i] != 0. 
Вызывать функцию не надо, только определите ее.

Sample Input:
1 6 2 2 4 4
6 5 3 3 2 4
Sample Output:
[False  True False False  True False]
'''
import numpy as np

def func1(a: np, b: np) -> np:
    arr = np.zeros(shape=a.size, dtype=bool)
    i = 0
    for x, y in zip(a, b):
        arr[i] = x > y and x != 0
        i += 1
    return arr

if __name__ == '__main__':
    print(
        func1(
            np.fromstring('1 6 2 2 4 4', sep=' '),
            np.fromstring('6 5 3 3 2 4', sep=' ')
        )
    )