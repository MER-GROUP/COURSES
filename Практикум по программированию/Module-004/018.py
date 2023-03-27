'''
Количество положительных
Найдите количество положительных элементов в данном списке.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
1 -2 3 -4 5
Sample Output:
3
'''
import sys
from array import array

# sys.stdin = open(file='018.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

print(sum(0 < i for i in arr))