'''
Четные элементы
Выведите все четные элементы списка.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
1 2 2 3 3 3 4
Sample Output:
2 2 4
'''
import sys
from array import array

# sys.stdin = open(file='017.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

print(*filter(lambda x: not(x % 2), arr))