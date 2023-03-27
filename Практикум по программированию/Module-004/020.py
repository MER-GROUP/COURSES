'''
Соседи одного знака
Дан список чисел. Если в нем есть два соседних элемента одного знака, 
выведите эти числа. Если соседних элементов одного знака нет - не выводите ничего. 
Если таких пар соседей несколько - выведите первую пару.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
-1 2 3 -1 -2
Sample Output:
2 3
'''
import sys
from array import array

# sys.stdin = open(file='020.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

for _i in range(1, len(arr)):
    if -1 < arr[_i-1] and -1 < arr[_i] or\
        0 > arr[_i-1] and 0 > arr[_i]:
        print(arr[_i-1], arr[_i])
        break