'''
Столбцы
Дана таблица N × N, заполненная целыми числами. 
Петр Первый считает столбец хорошим, если тот содержит число Х. 
Требуется для каждого столбца выяснить, является ли тот хорошим.

Входные данные
В первой строке число X, не превышающее по модулю 2*10^9. 
Во второй строке число N (1 <= N <= 100), В следующих N строках 
по N целых чисел, не превышающих по модулю 2*10^9 – числа в ячейках таблицы.

Выходные данные
Для каждого столбца выведите YES, если в нем есть число Х, 
и NO в противном случае. (Каждый ответ с новой строки)

Sample Input 1:
1789
1
1789
Sample Output 1:
YES

Sample Input 2:
9
3
1 2 9
3 4 5
6 7 8
Sample Output 2:
NO
NO
YES
'''
import sys
from array import array
# from copy import copy

sys.stdin = open(file='008.csv', mode='rt', encoding='utf-8', newline='')
nm, _, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(nm)
# print(tup)
# arr = array('i', map(int, tup.split()))
# print(arr)

# 1
for _arr in zip(*(map(int, el.split()) for el in tup)):
    print(('NO', 'YES')[int(nm) in _arr])

# 2
# print('---------------------------------------------')
_arr = [list(map(int, el.split())) for el in tup]
# print(*_arr, sep='\n') # test
for i in range(len(_arr[0])):
    for j in range(len(_arr)):
        if int(nm) == _arr[j][i]:
            print('YES')
            break
    else:
        print('NO')