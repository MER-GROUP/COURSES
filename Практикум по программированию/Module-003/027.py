'''
Две половинки
Дана строка. Разрежьте ее на две равные части 
(если длина строки — четная, а если длина строки нечетная, 
то длина первой части должна быть на один символ больше). 
Переставьте эти две части местами, результат запишите 
в новую строку и выведите на экран.

При решении этой задачи нельзя пользоваться инструкцией if.

Входные данные
Вводится строка.

Выходные данные
Выведите ответ на задачу.

Sample Input 1:
Hi
Sample Output 1:
iH

Sample Input 2:
Hello
Sample Output 2:
loHel
'''
import sys

# sys.stdin = open(file='027.csv', mode='rt', encoding='utf-8', newline='')
arr = sys.stdin.read()
# print(arr) # test

first = arr[: len(arr) // 2 + (len(arr) % 2)]
# print(first) # test
second = arr[len(first) :]
# print(second) # test
print(second + first)