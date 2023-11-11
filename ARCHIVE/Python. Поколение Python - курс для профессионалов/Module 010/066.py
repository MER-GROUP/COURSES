'''
Группы слов
Напишите программу, которая группирует слова по их длине.

Формат входных данных
На вход программе подается последовательность слов, разделенных пробелом. 
Каждое слово записано строчными латинскими буквами.

Формат выходных данных
Программа должна сгруппировать введенные слова по их длине и вывести полученные группы. 
Для каждой группы должна быть указана длина, а затем через запятую перечислены слова, 
имеющие соответствующую длину. Группы должны быть расположены в порядке увеличения длины, 
каждая на отдельной строке, слова в группах — в алфавитном порядке, в следующем формате:

<длина> -> <слово>, <слово>, ...
Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами.
https://stepik.org/media/attachments/lesson/674986/tests_2807349.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.11/Module_10.11.12

Sample Input 1:
hi never here my blue
Sample Output 1:
2 -> hi, my
4 -> blue, here
5 -> never

Sample Input 2:
hello beegeek stepik python
Sample Output 2:
5 -> hello
6 -> python, stepik
7 -> beegeek
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
import itertools as it

if __name__ == '__main__':
    words = input().split()
    words.sort(key=lambda x: (len(x), x))
    words_groupby = it.groupby(words, key=len)
    for key, group in words_groupby:
        print(f'{key} -> {", ".join(group)}')