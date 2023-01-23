'''
Сумма последовательности - 2
Найдите сумму последовательности натуральных чисел, 
если признаком окончания конца последовательности является 
два подряд идущих числа 0.

Числа, следующие после двух подряд идущих нулей считывать не нужно.

Входные данные
Вводится последовательность целых чисел, оканчивающаяся числом 0 
(само число 0 в последовательность не входит).

Выходные данные
Выведите ответ на задачу.

Sample Input:
1
0
7
0
9
0
0
Sample Output:
17
'''
import sys

# sys.stdin = open(file='098.csv', mode='rt', encoding='utf-8', newline='')
tup = tuple(map(int,sys.stdin.readlines()))
# arr = tup[: tup.index(0)]

arr = list()
n = None
n_prev = None
for i in tup:
    n, n_prev = i, n
    if 0 == n and 0 == n_prev:
        arr.pop()
        break
    arr.append(i)
print(sum(arr))