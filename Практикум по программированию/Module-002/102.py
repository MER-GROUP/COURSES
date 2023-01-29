'''
Наименьшее расстояние между локальными максимумами
Определите наименьшее расстояние между двумя локальными максимумами 
последовательности натуральных чисел, завершающейся числом 0. 
Если в последовательности нет двух локальных максимумов, 
выведите число 0.

Входные данные
Дана последовательность натуральных чисел, оканчивающаяся числом 0 
(само число 0 в последовательность не входит)

Выходные данные
Выведите ответ на задачу.

ЗЫ: Расстоянием считается количество пробелов между элементами. 
Пример на скриншоте ниже:

Sample Input:
1
2
1
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

# sys.stdin = open(file='102.csv', mode='rt', encoding='utf-8', newline='')
tup = tuple(map(int,sys.stdin.readlines()))
arr = tup[: tup.index(0)]

count_n = 0
prev_n, n, next_n = int(), arr[0], int()
check = False
min_n = float('infinity')

for i in range(1, len(arr)-1):
    prev_n, n, next_n = n, arr[i], arr[i+1]
    if prev_n < n > next_n:
        check = True
        if count_n and count_n < min_n:
            min_n = count_n
        count_n = 0
    if check: count_n += 1
print((0, min_n)[float('infinity') != min_n])