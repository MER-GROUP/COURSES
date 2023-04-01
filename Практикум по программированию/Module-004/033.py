'''
Количество совпадающих пар
Дан список чисел. Посчитайте, сколько в нем пар элементов, 
равных друг другу. Считается, что любые два элемента, 
равные друг другу образуют одну пару, которую необходимо посчитать.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input 1:
1 2 3 2 3
Sample Output 1:
2

Sample Input 2:
1 1 1 1 1
Sample Output 2:
10
'''
import sys
from array import array

# sys.stdin = open(file='033.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

_count = 0
for _i in range(len(arr)):
    for _j in range(_i+1, len(arr)):
        if arr[_i] == arr[_j]:
            _count += 1
print(_count)

# for i in range(15):
#     print(f'i = {i}')
#     print(f'i>>1 = {i>>1}')
#     print(f'i<<1 = {i<<1}')