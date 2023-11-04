'''
Функция multiple_split()

Реализуйте функцию multiple_split(), которая принимает два аргумента:

string — строка
delimiters — список строк

Функция должна разбивать строку string на подстроки, используя в качестве 
разделителей строки из списка delimiters, и возвращать полученный результат в виде списка.

Примечание 1. Другими словами, функция multiple_split() должна работать 
аналогично строковому методу split(), за тем исключением, что delimiters 
может содержать не единственный разделитель, а целый набор разделителей.

Примечание 2. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию multiple_split(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/699083/tests_2902499.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.9/Module_11.9.12

Sample Input 1:
print(multiple_split('beegeek-python.stepik', ['.', '-']))
Sample Output 1:
['beegeek', 'python', 'stepik']

Sample Input 2:
print(multiple_split('Timur---Arthur+++Dima****Anri', ['---', '+++', '****']))
Sample Output 2:
['Timur', 'Arthur', 'Dima', 'Anri']

Sample Input 3:
print(multiple_split('timur.^[+arthur.^[+dima.^[+anri.^[+roma.^[+ruslan', ['.^[+']))
Sample Output 3:
['timur', 'arthur', 'dima', 'anri', 'roma', 'ruslan']
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

def func(string: str) -> str:
    ...

if __name__ == '__main__':
    stdin = open(file='062-test.csv', mode='rt', encoding='utf-8', newline='')
    # sentense = map(str, stdin)
    sentense = stdin.read()
    print(sentense) # test
    print('------') # test
    pattern = rf''

    print(func(sentense), sep=', ')