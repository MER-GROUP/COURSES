'''
Вывести в обратном порядке
Выведите элементы данного списка в обратном порядке, не изменяя сам список.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
1 2 3 4 5
Sample Output:
5 4 3 2 1
'''
import sys
from array import array

# sys.stdin = open(file='027.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

print(*reversed(arr)) # 1
# print(*arr[::-1]) # 2
# # 3
# for i in range(len(arr)//2):
#     # print(f'i = {i}')
#     # print(f'~i = {~i}')
#     # arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
#     arr[i], arr[~i] = arr[~i], arr[i]
# print(*arr)