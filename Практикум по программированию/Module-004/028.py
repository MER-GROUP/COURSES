'''
Переставить соседние
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т.д.). 
Если элементов нечетное число, то последний элемент остается на своем месте.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
1 2 3 4 5
Sample Output:
2 1 4 3 5
'''
import sys
from array import array

# sys.stdin = open(file='028.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

for i in range(0, len(arr)-1, 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]
print(*arr)