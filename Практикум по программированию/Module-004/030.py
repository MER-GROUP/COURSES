'''
Переставить min и max
В списке все элементы различны. Поменяйте местами минимальный 
и максимальный элемент этого списка.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
3 4 5 2 1
Sample Output:
3 4 1 2 5
'''
import sys
from array import array

sys.stdin = open(file='030.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
print(arr) # test

pass