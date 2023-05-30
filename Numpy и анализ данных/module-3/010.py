'''
Массив numpy 3
На вход подается целое число n>=1. Создайте массив, 
содержащий n первых простых чисел. Выведите его на экран.

Sample Input:
3
Sample Output:
[2 3 5]
'''
import numpy as np

def simple_digits(n: int) -> list:
    _list = list()
    _digits = 2
    while True:
        _count = 0
        for i in range(1, _digits+1//2+1):
            if not _digits % i:
                _count += 1
            if 3 < _count:
                break
        if 2 >= _count:
            _list.append(_digits)
        if len(_list) == n:
            break
        _digits += 1
    return _list

print(np.array(simple_digits(int(input()))))