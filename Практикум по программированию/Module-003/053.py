'''
Количество совпадающих
Даны два списка чисел, которые могут содержать до 100000 чисел каждый. 
Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.

Примечание. Эту задачу на Питоне можно решить в одну строчку.

Входные данные
Вводятся два списка чисел. Все числа каждого списка находятся на отдельной строке.

Выходные данные
Выведите ответ на задачу.

Sample Input:
1 3 2
4 3 2
Sample Output:
2
'''
import sys

# sys.stdin = open(file='053.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.read().splitlines()))
# print(*arr, sep='\n') # test

print(len({i for i in map(int, arr[0].split())}.intersection({i for i in map(int, arr[1].split())})))