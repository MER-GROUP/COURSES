'''
Наименьший нечетный
Выведите значение наименьшего нечетного элемента списка, 
а если в списке нет нечетных элементов - выведите число 0.

Входные данные
Вводится список чисел. Все числа списка находятся на одной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input 1:
0 1 2 3 4
Sample Output 1:
1

Sample Input 2:
2 4 6 8 10
Sample Output 2:
0
'''
import sys
from array import array

# sys.stdin = open(file='024.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
arr = array('i', list(map(int, arr[0].split())))
# print(arr) # test

# print(min(filter(lambda x: x % 2, arr)) if len(list(filter(lambda x: x % 2, arr))) else 0) # 1

# 2
_min = float('inf')
for _el in arr:
    if _min > _el and _el % 2:
        _min = _el
# print(_min if not _min == float('inf') else 0)
print((_min, 0)[_min == float('inf')])

# 3
print(min(
    [x for x in map(int, input().split()) if x % 2] + [0], 
    key=lambda x: (x==0, x))
)