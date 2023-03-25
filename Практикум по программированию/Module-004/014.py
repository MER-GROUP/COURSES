'''
Суперсдвиг
Дана последовательность из N (1 ≤ N ≤ 100000) целых чисел и число K (|K| ≤ 100000). 
Сдвинуть всю последовательность (сдвиг - циклический) на |K| элементов вправо, 
если K – положительное и влево, если отрицательное.

В данной задаче нельзя использовать дополнительные массивы (списки). 
Обратите внимание, что нужно именно преобразовать имеющийся список и распечатать его целиком, 
а не создать новый, даже назвав его тем же самым именем (это возможно в языке Python).

Входные данные
В первой строке дано натуральное число N, во второй строке N целых чисел, 
а в последней целое число K. Все числа во входных данных не превышают 10^9.

Выходные данные
Требуется вывести полученную последовательность. Числа следует выводить через пробел.

Sample Input:
5
5 3 7 4 6
3
Sample Output:
7 4 6 5 3
'''
import sys
from array import array
from copy import copy

# sys.stdin = open(file='014.csv', mode='rt', encoding='utf-8', newline='')
_, *arr, shift = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
print(arr) # test

# O(2N)
_arr = copy(arr)
if 0 < int(shift):
    for _ in range(int(shift)):
        for _i in range(1, len(_arr)):
            _arr[_i-1], _arr[-1] = _arr[-1], _arr[_i-1]
else:
    for _ in range(abs(int(shift))):
        for _i in range(-1, -len(_arr), -1):
            _arr[_i], _arr[0] = _arr[0], _arr[_i]
print(*_arr)

# O(N)
_arr3 = copy(arr)
print(*[_arr3[(_ - int(shift)) % len(_arr3)] for _ in range(len(_arr3))])