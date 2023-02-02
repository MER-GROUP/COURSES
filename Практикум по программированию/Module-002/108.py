'''
Количество палиндромов
Назовем число палиндромом, если оно не меняется 
при перестановке его цифр в обратном порядке. 
Напишите программу, которая по заданному числу 
K выводит количество натуральных палиндромов, 
не превосходящих K.

Входные данные
Задано единственное число K (1 ≤ K ≤ 100000).

Выходные данные
Необходимо вывести количество натуральных палиндромов, 
не превосходящих K.

Sample Input:
1
Sample Output:
1
'''
import sys

# sys.stdin = open(file='108.csv', mode='rt', encoding='utf-8', newline='')
tup = sys.stdin.read()

print(
    sum(
        map(
            lambda x: str(x) == str(x)[::-1],
            range(1, int(tup)+1)
        )
    )
)