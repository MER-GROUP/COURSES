'''
Наименьший положительный
Выведите значение наименьшего из всех положительных элементов в списке. 
Известно, что в списке есть хотя бы один положительный элемент, 
а значения всех элементов списка по модулю не превосходят 1000.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
5 -4 3 -2 1
Sample Output:
1
'''
import sys
from array import array

sys.stdin = open(file='023.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
print(arr) # test

pass