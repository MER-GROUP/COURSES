'''
Beegeek

Напишите программу, определяющую:

количество строк, в которых bee встречается в качестве подстроки не менее двух раз
количество строк, в которых geek встречается в качестве слова хотя бы один раз

Формат входных данных
На вход программе произвольное количество строк, каждая из которых содержит 
набор произвольных символов.

Формат выходных данных
Программа должна вывести два числа:

первое — количество строк, в которых bee встречается в качестве подстроки не менее двух раз
второе — количество строк, в которых geek встречается в качестве слова хотя бы один раз
каждое на отдельной строке.

Примечание 1. Словом будем считать любую непрерывную последовательность из одного 
или нескольких символов, соответствующих \w.

Примечание 2. Строка может одновременно удовлетворять обоим условиям.

Примечание 3. В первой строке первого теста bee встречается в качестве подстроки 3 раза:

beebee bee

Во второй строке bee встречается в качестве подстроки лишь один раз, а слово geek отсутствует.

В третьей строке bee встречается в качестве подстроки 2 раза, geek в качестве слова — 1 раз:

bee geek bee

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680263/tests_2896123.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.6/Module_11.6.12

Sample Input 1:
beebee bee
beegeek
bee geek bee
Sample Output 1:
2
1

Sample Input 2:
abigail alex
clint dwarf
emily
gil
Sample Output 2:
0
0
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

if __name__ == '__main__':
    stdin = open(file='041-test.csv', mode='rt', encoding='utf-8', newline='')
    pattern_bee = r'(bee)[\w\s]*\1'
    pattern_geek = r'\b(geek)\b'
    bee, geek = [0] * 2
    
    for word in map(str.strip, stdin):
        search_bee = re.search(pattern_bee, word)
        search_geek = re.search(pattern_geek, word)
        if search_bee:
            bee += 1
        if search_geek:
            geek += 1
    
    print(bee, geek, sep='\n')