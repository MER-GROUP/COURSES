'''
Количество различных элементов
Дан список, упорядоченный по неубыванию элементов в нем. 
Определите, сколько в нем различных элементов.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
1 2 2 3 3 3
Sample Output:
3
'''
import sys
from array import array

# sys.stdin = open(file='026.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

# print(len(set(arr))) # 1

print(sum(arr[i-1] < arr[i] for i in range(1, len(arr))) + 1) # 2