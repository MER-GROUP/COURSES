'''
reverse array

Напишите функцию reverse_array(arr), которая принимает на вход одномерный массив arr 
и возвращает новый массив с элементами arr, расположенными в обратном порядке.

Функцию вызывать не нужно, просто создайте ее.

Sample Input:
76 55 60 81 87 84 71 52 79 86 84 83 76 72 69 71 99 84 90 82 62
Sample Output:
[62 82 90 84 99 71 69 72 76 83 84 86 79 52 71 84 87 81 60 55 76]
'''
import numpy as np

def reverse_array(arr: np) -> np:
    return arr.copy()[::-1]

if __name__ == '__main__':
    arr = np.array('76 55 60 81 87 84 71 52 79 86 84 83 76 72 69 71 99 84 90 82 62'.split(), dtype=int)
    print(reverse_array(arr))