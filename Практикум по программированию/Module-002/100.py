'''
Максимальная длина монотонного фрагмента
Дана последовательность натуральных чисел, завершающаяся числом 0. 
Определите наибольшую длину монотонного фрагмента последовательности 
(то есть такого фрагмента, где все элементы, кроме первого, 
либо больше предыдущего, либо меньше).

Гарантируется, что в последовательности не менее двух чисел, 
отличных друг от друга.

Числа, следующие за числом 0, считывать не нужно.

Входные данные
Дана последовательность натуральных чисел, завершающаяся числом 0 
(ноль не входит в последовательность).

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
4
5
6
7
0
Sample Output 2:
7
'''
import sys

# sys.stdin = open(file='100.csv', mode='rt', encoding='utf-8', newline='')
tup = tuple(map(int,sys.stdin.readlines()))
arr = tup[: tup.index(0)]

max_up, max_down = 1, 1
count_up_n, count_down_n = 1, 1
prev_n, n = int(), arr[0]

for i in arr[1:]:
    n, prev_n = i, n
    if n > prev_n:
        count_up_n += 1
        if count_up_n > max_up:
            max_up = count_up_n
        count_down_n = 1
    if n < prev_n:
        count_down_n += 1
        if count_down_n > max_down:
            max_down = count_down_n
        count_up_n = 1
    if n == prev_n:
        count_up_n = 1
        count_down_n = 1

print(max(max_up, max_down))