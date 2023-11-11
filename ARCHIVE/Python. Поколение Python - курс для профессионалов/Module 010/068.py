'''
Функция group_anagrams()
Анаграммы — это слова, которые состоят из одинаковых букв. Например:

адаптер — петарда
адресочек — середочка
азбука — базука
аистенок — осетинка

Реализуйте функцию group_anagrams(), которая принимает один аргумент:

words — список слов

Функция должна группировать в кортежи слова из списка words, являющиеся анаграммами, 
и возвращать список полученных кортежей.

Примечание 1. Порядок кортежей в возвращаемом функцией списке, а также порядок элементов 
в этих кортежах, не важен.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию group_anagrams(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/674986/tests_2797014.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.11/Module_10.11.14

Sample Input 1:
groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])
print(*groups)
Sample Output 1:
('boko', 'book') ('evil', 'levi', 'live') ('afther', 'father')

Sample Input 2:
groups = group_anagrams(['evil', 'father', 'book', 'stepik', 'beegeek'])
print(*groups)
Sample Output 2:
('beegeek',) ('book',) ('evil',) ('father',) ('stepik',)

Sample Input 3:
groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])
print(*groups)
Sample Output 3:
('крона', 'норка') ('сеточка', 'тесачок', 'стоечка') ('лучик', 'чулки')
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
import itertools as it
from collections import Counter

def group_anagrams(words: list[str]) -> list[str]:
    words.sort(key=len)
    words_groupby = it.groupby(words, key=len)
    anagrams = list()
    for _, group in words_groupby:
        arr = list(group)
        while arr:
            anagrams.append([arr.pop(0)])
            i = 0
            while i < len(arr):
                if Counter(anagrams[-1][0]) == Counter(arr[i]):
                    anagrams[-1].extend([arr.pop(i)])
                    i -= 1
                i += 1
    anagrams = list(map(tuple, anagrams))
    return anagrams

if __name__ == '__main__':
    groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther', 'boko'])
    print(*groups)

    groups = group_anagrams(['evil', 'father', 'book', 'stepik', 'beegeek'])
    print(*groups)

    groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])
    print(*groups)