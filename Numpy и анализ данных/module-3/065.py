'''
swap first last

Напишите функцию swap_first_last(arr), которая принимает на вход одномерный массив arr 
и возвращает новый массив, в котором первый и последний элементы поменялись местами.

Sample Input:
0 82 62 71 56 78 59 97 77 78 85 73 60 72 52 64 95 5
Sample Output:
[ 5 82 62 71 56 78 59 97 77 78 85 73 60 72 52 64 95  0]
'''
import numpy as np

def swap_first_last(arr: np) -> np:
    _arr = arr.copy()
    _arr[0], _arr[-1] = arr[-1], arr[0]
    return _arr

if __name__ == '__main__':
    print(
        swap_first_last(
            np.array(
                object='0 82 62 71 56 78 59 97 77 78 85 73 60 72 52 64 95 5'.split(),
                dtype=int
            )
        )
    )