'''
Вставить элемент
Дан список целых чисел, число k и значение C. Необходимо вставить 
в список на позицию с индексом k элемент, равный C, сдвинув все элементы, 
имевшие индекс не менее k, вправо.

Поскольку при этом количество элементов в списке увеличивается, 
после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого 
при выводе и не создавая дополнительного списка.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке. 
На второй строке вводятся числа k и C.

Выходные данные
Выведите ответ на задачу.

Sample Input:
7 6 5 4 3 2 1
2 0
Sample Output:
7 6 0 5 4 3 2 1
'''
import sys
from array import array
from copy import copy

# sys.stdin = open(file='032.csv', mode='rt', encoding='utf-8', newline='')
arr, _str = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr.split())))
_index, _value = map(int, _str.split())
# print(arr) # test
# print(_index) # test
# print(_value) # test  

# # 1
# _arr = copy(arr)
# _arr.insert(_index, _value)
# print(*_arr)

# # 2
# _arr2 = copy(arr)
# _arr2.append(_value)
# for _i in range(len(_arr2)-1, _index, -1):
#     _arr2[_i-1], _arr2[_i] = _arr2[_i], _arr2[_i-1]
# print(*_arr2)

# 3
_arr3 = copy(arr)
_arr3.append(_value)
for _i in range(_index, len(_arr3)):
    _arr3[_i], _arr3[-1] = _arr3[-1], _arr3[_i]
print(*_arr3)