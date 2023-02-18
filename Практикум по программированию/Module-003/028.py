'''
Переставить два слова

Дана строка, состоящая ровно из двух слов, разделенных пробелом. 
ереставьте эти слова местами. Результат запишите в строку 
и выведите получившуюся строку.

При решении этой задачи нельзя пользоваться циклами и инструкцией if.

Входные данные
Вводится строка.

Выходные данные
Выведите ответ на задачу.

Sample Input:
Hello, world!
Sample Output:
world! Hello,
'''
import sys

# sys.stdin = open(file='028.csv', mode='rt', encoding='utf-8', newline='')
arr = sys.stdin.read()
# print(arr) # test

print(arr[arr.find(' ')+1 :] + ' ' + arr[: arr.find(' ')])