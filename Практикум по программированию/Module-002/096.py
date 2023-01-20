'''
Второй максимум - 2
Последовательность состоит из натуральных чисел и завершается числом 0. 
Определите значение второго по величине элемента в этой последовательности, 
то есть элемента, который будет наибольшим, если из последовательности 
удалить наибольший элемент.

Числа, следующие за числом 0, считывать не нужно.

Входные данные
Вводится последовательность целых чисел, оканчивающаяся числом 0 
(само число 0 в последовательность не входит).

Выходные данные
Выведите ответ на задачу.

Sample Input:
1
7
9
0
Sample Output:
7

Sample Input:
8
9
9
9
7
7
8
0
Sample Output:
8

Sample Input:
7
7
6
5
0
Sample Output:
6
'''
import sys

# sys.stdin = open(file='096.csv', mode='rt', encoding='utf-8', newline='')
tup = tuple(map(int,sys.stdin.readlines()))
arr = tup[: tup.index(0)]

max_n = arr[0]
max_prev_n = float('-Infinity')
for i in arr[1:]:
    if i > max_n:
        max_n, max_prev_n = i, max_n
    elif i > max_prev_n and not i == max_n:
        max_prev_n = i
print(max_prev_n)

print(sorted(set(arr))[-2])