'''
Вставка символов
Дана строка. Получите новую строку, вставив между двумя символами 
исходной строки символ *. Выведите полученную строку.

Входные данные
Вводится строка.

Выходные данные
Выведите ответ на задачу.

Sample Input:
Python
Sample Output:
P*y*t*h*o*n
'''
import sys  

# sys.stdin = open(file='037.csv', mode='rt', encoding='utf-8', newline='')
arr = sys.stdin.read()
# print(arr) # test

# print('*'.join(list(arr)))
print('*'.join(arr))