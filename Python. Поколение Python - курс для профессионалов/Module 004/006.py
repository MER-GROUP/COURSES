'''
Без комментариев
Дан блок кода на языке Python. Напишите программу, 
которая удаляет все строки в данном коде, 
которые содержат в себе только комментарии. 
Если в строке помимо комментария имеется что-то еще, 
то такую строку учитывать не нужно.

Формат входных данных
На вход программе подается произвольное количество строк, 
в совокупности представляющих блок кода на языке Python.

Формат выходных данных
Программа должна вывести введенный блок кода, 
предварительно удалив из него все строки которые содержат в себе только комментарии.

Примечание 1. Порядок вывода строк кода должен совпадать с порядком их ввода.

Примечание 2. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/520159/tests_2534824.zip

Sample Input:

digit = int(input())
s = input()
for i in s:
    #комментирую потому что прикольно

    if 97 > ord(i) - digit:
        temp = ord(i) - digit + 26
        print(chr(temp), end='')   #вывод
    else:
        #ахаха
        temp = ord(i) - digit
        print(chr(temp), end='')

Sample Output:

digit = int(input())
s = input()
for i in s:

    if 97 > ord(i) - digit:
        temp = ord(i) - digit + 26
        print(chr(temp), end='')   #вывод
    else:
        temp = ord(i) - digit
        print(chr(temp), end='')
'''
import sys

arr = [i for i in sys.stdin if not i.strip().startswith('#')]
sys.stdout.writelines(arr)