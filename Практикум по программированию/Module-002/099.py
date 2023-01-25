'''
Максимальное число идущих подряд равных элементов
Дана последовательность натуральных чисел, 
завершающаяся числом 0. Определите, какое наибольшее 
число подряд идущих элементов этой последовательности 
равны друг другу. Если все элементы разные, 
максимальным числом будет 1.

Числа, следующие за числом 0, считывать не нужно.

Входные данные
Дана последовательность натуральных чисел, завершающаяся числом 0.

Выходные данные
Выведите ответ на задачу.

Sample Input 1:
1
7
7
9
1
0
Sample Output 1:
2

Sample Input 2:
1
2
3
0
Sample Output 2:
1
'''
import sys

# sys.stdin = open(file='099.csv', mode='rt', encoding='utf-8', newline='')
tup = tuple(map(int,sys.stdin.readlines()))
arr = tup[: tup.index(0)]

max_n, count_n = 1, 1
n, prev_n = None, None

for i in arr:
    n, prev_n = i, n
    if n == prev_n:
        count_n += 1
        if count_n > max_n:
            max_n = count_n
    else:
        count_n = 1
print(max_n)