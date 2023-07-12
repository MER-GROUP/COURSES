'''
slice replace

Напишите функцию slice_replace(arr, start, end, replacement), которая принимает на 
вход список arr, начальный и конечный индексы среза start и end, а также новый 
список replacement, который будет использоваться для замены элементов из 
среза arr[start:end]. Функция должна возвращать новый NumPy массив, в котором 
элементы среза arr[start:end] заменены на элементы среза списка replacement[start:end].

При этом

Если start > last_index, где last_index - последний индекс массива arr, 
и start<last_index_replacement,  то элементы среза replacement[start:end] 
добавляются в конец массива arr.

Если start > last_index_replacement, то массив arr возвращается без изменений.

Sample Input:
76 55 60 81 87 84 71 52 79 86 84
0
5
91 59 53 79 58 91 81 67 58 56 76 54 85
Sample Output:
[91 59 53 79 58 84 71 52 79 86 84]
'''
import numpy as np

def slice_replace(arr: list, start: int, end: int, replacement: list) -> np:
    last_index = len(arr) - 1
    last_index_replacement = len(replacement) - 1

    if start > last_index_replacement:
        return np.array(object=arr).astype(int)
    elif start > last_index and start<last_index_replacement:
        return np.concatenate((arr, replacement[start : end])).astype(int)
    else:
        return np.concatenate((arr[:start], replacement[start : end], arr[end:])).astype(int)

if __name__ == '__main__':
    arr = list(map(int, '76 55 60 81 87 84 71 52 79 86 84'.split()))
    start = 0
    end = 5
    replacement = list(map(int, '91 59 53 79 58 91 81 67 58 56 76 54 85'.split()))
    print(slice_replace(arr, start, end, replacement))