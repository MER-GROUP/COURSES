'''
Вставка числа
Требуется вставить в данный массив на данное место данный элемент, 
сдвинув остальные элементы вправо.

Входные данные
В первой строке вводится одно натуральное число, не 
превосходящее 1000 – размер массива. Во второй строке задаются 
N чисел – элементы массива (целые числа, не превосходящие по модулю 1000). 
В третьей строке вводится число, которое необходимо вставить, 
и номер места, на которое его нужно вставить.

Выходные данные
Вывести получившийся массив.

Sample Input:
5
1 2 3 4 5
2 3
Sample Output:
1 2 2 3 4 5
'''
import sys
from array import array
from copy import copy

sys.stdin = open(file='018.csv', mode='rt', encoding='utf-8', newline='')
_, *tup = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(tup)
arr1 = array('i', map(int, tup[0].split()))
# print(arr1)
di = array('i', map(int, tup[1].split()))
# print(di)

# 1
arr2 = copy(arr1)
arr2.insert(di[1]-1, di[0])
print(*arr2)

# 2
arr3 = list()
for i in range(len(arr1)):
    if di[1]-1 == i:
        arr3.append(di[0])
    arr3.append(arr1[i])
print(*arr3)