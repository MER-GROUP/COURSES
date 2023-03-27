'''
Больше предыдущего
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
1 5 2 4 3
Sample Output:
5 4
'''
import sys
from array import array

# sys.stdin = open(file='019.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

print(*(arr[i] for i in range(1, len(arr)) if arr[i] > arr[i-1]))