'''
Количество различных элементов - 2
Дан список. Посчитайте, сколько в нем различных элементов, 
не изменяя самого списка.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
3 2 1 2 3
Sample Output:
3
'''
import sys
from array import array

# sys.stdin = open(file='035.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

# print(len(set(arr))) # 1

# 2
_visited = list()
for _el in arr:
    if _el not in _visited:
        _visited.append(_el)
print(len(_visited))