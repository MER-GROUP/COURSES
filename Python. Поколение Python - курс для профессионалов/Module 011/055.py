'''
Ключевые слова

В Python существуют ключевые слова, которые нельзя использовать для названия переменных, 
функций и классов. Для получения списка всех ключевых слов можно воспользоваться 
атрибутом kwlist из модуля keyword.

Приведенный ниже код:

import keyword

print(keyword.kwlist)

выводит:

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
'return', 'try', 'while', 'with', 'yield']

Напишите программу, которая принимает строку текста и заменяет в ней все ключевые слова на <kw>.

Формат входных данных
На вход программе подается строка.

Формат выходных данных
Программа должна в введенном тексте заменить все ключевые слова (в любом регистре) 
на строку <kw> и вывести полученный результат.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680266/tests_2907187.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.8/Module_11.8.11

Sample Input 1:
True, assert, as, false, or, Import
Sample Output 1:
<kw>, <kw>, <kw>, <kw>, <kw>, <kw>

Sample Input 2:
True or False - that's the question
Sample Output 2:
<kw> <kw> <kw> - that's the question

Sample Input 3:
True and False - that is the question
Sample Output 3:
<kw> <kw> <kw> - that <kw> the question
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin
# from collections import defaultdict

def normalize_whitespace(string: str) -> str:
    return re.sub(
        pattern=r'\s{2,}',
        repl=r' ',
        string=string
    )

if __name__ == '__main__':
    stdin = open(file='055-test.csv', mode='rt', encoding='utf-8', newline='')
    # sentense = map(str.strip, stdin)
    sentense = stdin.read()
    print(sentense) # test
    print('------') # test
    pattern = rf''

    print(normalize_whitespace(sentense))