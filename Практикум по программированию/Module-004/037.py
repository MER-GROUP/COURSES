'''
Сжатие списка
Дан список целых чисел. Требуется “сжать” его, переместив 
все ненулевые элементы в левую часть списка, не меняя их порядок, 
а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя, 
дополнительный список использовать нельзя, 
задачу нужно выполнить за один проход по списку. Распечатайте полученный список.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
4 0 5 0 3 0 0 5
Sample Output:
4 5 3 5 0 0 0 0
'''
import sys
from array import array
from copy import copy

sys.stdin = open(file='037.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
print(arr) # test

# 1
_arr = copy(arr)
_len = len(_arr)
_i = 0
while 0 < _len:
    if 0 == _arr[_i]:
        _arr.append(_arr.pop(_i))
    else:
        _i += 1
    _len -= 1
print(*_arr)

# 2
_arr2 = copy(arr)
_count = 0
_i = 0
while _i < len(_arr2):
    if 0 == _arr2[_i]:
        del _arr2[_i]
        _count += 1
        continue
    _i += 1
_arr2.extend([0]*_count)
print(*_arr2)

# 3
lst = copy(arr)
zpos = 0
for i in range(len(lst)):
    if lst[i]:
        lst[zpos], lst[i] = lst[i], lst[zpos]
        zpos += 1
print(*lst)  

# 4
lst2 = copy(arr)
print(*sorted(lst2, key=lambda x: x == 0))