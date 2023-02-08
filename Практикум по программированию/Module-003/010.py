'''
Совпадают ли строки?
Необходимо определить, совпадают ли 2 строки.

Входные данные
Заданы 2 строки.

Выходные данные
Необходимо вывести  слово yes, если строки совпадают, 
и слово no в противном случае.

Sample Input:
a
a
Sample Output:
yes
'''
import sys

# sys.stdin = open(file='010.csv', mode='rt', encoding='utf-8', newline='')
arr = list(map(str.strip, sys.stdin))

print(('no', 'yes')[arr[0] == arr[1]])