'''
Уникальные элементы
Дан список. Выведите те его элементы, которые встречаются в списке 
только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
1 2 2 3 3 3
Sample Output:
1
'''
import sys
from array import array

sys.stdin = open(file='034.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
print(arr) # test

pass