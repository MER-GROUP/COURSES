'''
Количество локальных максимумов
Элемент последовательности называется локальным максимумом, 
если он строго больше предыдущего и последующего элемента последовательности. 
Первый и последний элемент последовательности не являются локальными максимумами.

Дана последовательность натуральных чисел, признаком конца которой является число 0. 
Определите количество строгих локальных максимумов в этой последовательности. 

Числа, следующие за числом 0, считывать не нужно.

Входные данные
Дана последовательность натуральных чисел, признаком конца которой является число 0.

Выходные данные
Выведите ответ на задачу.

Sample Input:
1
2
1
2
1
0
Sample Output:
2
'''
import sys

# sys.stdin = open(file='101.csv', mode='rt', encoding='utf-8', newline='')
tup = tuple(map(int,sys.stdin.readlines()))
arr = tup[: tup.index(0)]

count_n = 0
prev_n, n, next_n = int(), arr[0], int()

for i in range(1, len(arr)-1):
    prev_n, n, next_n = n, arr[i], arr[i+1]
    if prev_n < n > next_n:
        count_n += 1
print(count_n)