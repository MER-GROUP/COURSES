'''
Количество нулей

Входные данные
Задано единственное число N, не больше 1000.

Выходные данные
Необходимо вывести количество нулей среди всех цифр числа N.

Sample Input:
100
Sample Output:
2
'''
import sys

# sys.stdin = open(file='104.csv', mode='rt', encoding='utf-8', newline='')
tup = sys.stdin.read()

print(
    len(
        tuple(
            filter(
                lambda x: '0' == x,
                tup
            )
        )
    )
)