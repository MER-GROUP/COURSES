'''
Перестановки
Напишите программу, которая выводит все перестановки символов строки без дубликатов.

Формат входных данных
На вход программе подается произвольная строка из строчных латинских букв, длина которой 
не превышает 10 символов.

Формат выходных данных
Программа должна вывести все перестановки символов данной строки без дубликатов 
в алфавитном порядке, каждую на отдельной строке.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680669/tests_2817309.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.12/Module_10.12.11

Sample Input 1:
aab
Sample Output 1:
aab
aba
baa

Sample Input 2:
abc
Sample Output 2:
abc
acb
bac
bca
cab
cba

Sample Input 3:
ab
Sample Output 3:
ab
ba

Sample Input 4:
a
Sample Output 4:
a
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
import itertools as it

def my_perm(s: str)->Iterator|Generator:
    return it.permutations(s)

if __name__ == '__main__':
    for t in sorted(set(my_perm(input()))):
        print(*t, sep='')

    # print(*it.permutations('aab', r=None))
    # print(*it.combinations('aab', r=2))