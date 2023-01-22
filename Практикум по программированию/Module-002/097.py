'''
Количество элементов, равных максимуму
Последовательность состоит из натуральных чисел и завершается числом 0. 
Всего вводится не более 10000 чисел (не считая завершающего числа 0). 
Определите, сколько элементов этой последовательности равны ее наибольшему элементу.

Числа, следующие за числом 0, считывать не нужно.

Входные данные
Вводится последовательность целых чисел, оканчивающаяся числом 0 
(само число 0 в последовательность не входит).

Выходные данные
Выведите ответ на задачу.

Sample Input:
1
3
3
1
0
Sample Output:
2
'''
import sys

# sys.stdin = open(file='097.csv', mode='rt', encoding='utf-8', newline='')
tup = tuple(map(int,sys.stdin.readlines()))
arr = tup[: tup.index(0)]

print(arr.count(max(arr)))

max_n = float('-infinity')
count_n = 0
for i in arr:
    if i > max_n:
        max_n = i
        count_n = 0
    if max_n == i:
        count_n += 1
print(count_n)

import heapq
count_n = 1
max_n, *arr = heapq.nlargest(len(arr), arr)
for i in arr:
    if i == max_n:
        count_n += 1
    else:
        break
print(count_n)