'''
Комментарии 🌶️🌶️

При написании программ мы нередко оставляем комментарии или строки-документации к функциям. Определим три вида комментариев:

однострочные комментарии — строки кода, начинающиеся с символа решетки #. Однострочные комментарии могут находиться на любом уровне вложенности. Например: 

# это однострочный комментарий

def func(a, b):
    # это однострочный комментарий
    return a + b

комментарии, следующие непосредственно за строкой кода. Другими словами, это строка кода, за которой следуют 22 пробела, символ решетки #, пробел и сам комментарий, например:

numbers = [1, 2, 3]  # это комментарий

многострочные комментарии — одна или несколько строк кода, которые начинаются и заканчиваются тремя кавычками """. Многострочные комментарии могут находиться на любом уровне вложенности. Например:

"""это многострочный комментарий"""

def func(a, b):
    """это
    многострочный
    комментарий"""
    return a + b

Напишите программу, которая удаляет все комментарии из Python кода.

Формат входных данных
На вход программе подается произвольное число строк, представляющих собой Python код.

Формат выходных данных
Программа должна удалить все комментарии из введенного кода согласно условию задачи 
и вывести полученный результат.

Примечание 1. Гарантируется, что комментарий, следующий за строкой кода, определяется 
однозначно. Другими словами, в самих строках кода не используется символ #.

Примечание 2. Пустые строки в начале и конце всего Python кода, а также пробелы 
в конце строк кода при сравнении ответов не учитываются. Другими словами, записи:



def func(a, b):
    return a + b
def func(a, b):
    return a + b
def func(a, b):
    return a + b


считаются одинаковыми.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680266/tests_2896133.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.8/Module_11.8.15

Sample Input:

"""hello everyone
welcome to my project"""

import math  # importing a useful math module

# let's take a look at some functions

def circle_area(radius):
    """coming soon"""
    return math.pi * r ** 2  # my favorite formula
    
def triangle_area(base, height):
    """the function takes
    the base and height
    of a triangle and
    returns its area"""
    return 0.5 * base * height

Sample Output:


import math


def circle_area(radius):
    return math.pi * r ** 2
    
def triangle_area(base, height):
    return 0.5 * base * height
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

def func(string: str) -> str:
    ...

if __name__ == '__main__':
    stdin = open(file='059-test.csv', mode='rt', encoding='utf-8', newline='')
    # sentense = map(str, stdin)
    sentense = stdin.read()
    print(sentense) # test
    print('------') # test
    pattern = rf''

    print(func(sentense))