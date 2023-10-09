'''
Одинаковые слоги

Напишите программу, которая выводит слова, состоящие из двух одинаковых слогов.

Формат входных данных
На вход программе подается произвольное количество слов, каждое на отдельной строке.

Формат выходных данных
Программа должна из введенных слов вывести только те, которые состоят из двух одинаковых 
слогов. Слова должны быть расположены в своем исходном порядке, каждое на отдельной строке.

Примечание 1. Словом будем считать любую непрерывную последовательность из одного или 
нескольких символов, соответствующих \w.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680263/tests_2891547.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.6/Module_11.6.11

Sample Input 1:
Python
beebee
PyPy
portal
Sample Output 1:
beebee
PyPy

Sample Input 2:
gogo
hohoho
XaXaXaXa
Sample Output 2:
gogo
XaXaXaXa
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

if __name__ == '__main__':
    stdin = open(file='040-test.csv', mode='rt', encoding='utf-8', newline='')
    pattern = r''
    
    pass