'''
Функция normalize_whitespace()

Реализуйте функцию normalize_whitespace(), которая принимает один аргумент:

string — произвольная строка

Функция должна заменять все множественные пробелы в строке string на единственный 
пробел и возвращать полученный результат.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию normalize_whitespace(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680266/tests_2902178.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.8/Module_11.8.10

Sample Input 1:
print(normalize_whitespace('AAAA                A                AAAA'))
Sample Output 1:
AAAA A AAAA

Sample Input 2:
print(normalize_whitespace('Тут нет лишних пробелов'))
Sample Output 2:
Тут нет лишних пробелов

Sample Input 3:
print(normalize_whitespace('Тут   н   е   т     л   и     шних пробелов     '))
Sample Output 3:
Тут н е т л и шних пробелов 
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin
# from collections import defaultdict

def normalize_whitespace(string: str) -> str:
    ...

if __name__ == '__main__':
    stdin = open(file='054-test.csv', mode='rt', encoding='utf-8', newline='')
    # sentense = map(str.strip, stdin)
    sentense = stdin.read()
    print(sentense) # test
    print('------') # test
    pattern = rf''

    pass