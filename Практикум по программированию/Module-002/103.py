'''
Сумма цифр числа

Входные данные
Задано единственное число N, не больше 1000.

Выходные данные
Необходимо вывести  сумму цифр числа N.

Sample Input:
42
Sample Output:
6
'''
import sys

# sys.stdin = open(file='103.csv', mode='rt', encoding='utf-8', newline='')
tup = sys.stdin.read()

print(
    sum(
        map(
            int,
            tup
        )
    )
)

s = 0
while int(tup):
    s += int(tup) % 10
    tup = int(tup) // 10
print(s)