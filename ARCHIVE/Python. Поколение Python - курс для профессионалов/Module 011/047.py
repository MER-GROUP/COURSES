'''
Слова

Напишите программу, которая принимает на вход строку текста и некоторое 
слово и определяет, сколько вхождений данного слова содержится в введенном тексте.

Формат входных данных
На вход программе на первой строке подается текст, на второй — слово.

Формат выходных данных
Программа должна определить, сколько вхождений данного слова содержится 
в веденном тексте, и вывести полученный результат.

Примечание 1. Словом будем считать последовательность символов, 
соответствующих \w, окруженную символами, соответствующими \W.

Примечание 2. Рассмотрим первый тест, в котором содержится 6 вхождений 
слова foo:

"foo" bar ("foo") bar "foo"-bar foo_bar "foo"'bar bar-"foo" bar, "foo".
foo_bar же является самостоятельным словом.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680265/tests_2830462.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.7/Module_11.7.12

Sample Input 1:
foo bar (foo) bar foo-bar foo_bar foo'bar bar-foo bar, foo.
foo
Sample Output 1:
6

Sample Input 2:
Sunday, Monday, Tuesday, Wednesday
day
Sample Output 2:
0

Sample Input 3:
Hhelo Hey Human hacker
H
Sample Output 3:
0
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

if __name__ == '__main__':
    stdin = open(file='047-test.csv', mode='rt', encoding='utf-8', newline='')
    text, word = map(str.strip, stdin)
    # print(text, word, sep='\n') # test
    pattern = rf'\b{word}\b'

    print(
        len(
            re.findall(
                pattern,
                text
            )
        )
    )