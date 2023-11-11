'''
Все еще достоин
Дан список имен учеников и их оценок за экзамен. Напишите программу, 
которая определяет второго по счету ученика, имеющего самую низкую оценку.

Формат входных данных
На вход программе подается произвольное количество строк, в каждой из которых 
записаны имя очередного ученика и его оценка, разделенные пробелом.

Формат выходных данных
Программа должна определить второго по счету ученика, который имеет самую низкую оценку, 
и вывести его имя.

Примечание 1. Гарантируется, что все ученики имеют различные имена и оценки.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/635441/tests_3091740.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_6/Module_6.8/Module_6.8.16

Sample Input 1:
Тимур 100
Анри 88
Дима 94
Артур 82
Владимир 90
Sample Output 1:
Анри

Sample Input 2:
Эллиот 100
Эбигейл 99
Марни 98
Винсент 97
Кробус 96
Пенни 95
Sample Output 2:
Кробус
'''
from collections import Counter, defaultdict, namedtuple
student = namedtuple('student', ('name', 'mark'))
import sys
# sys.stdin = open(file='026-tests.csv', mode='rt', encoding='utf-8', newline='')

_tuple = tuple(
    student(name=_name, mark=int(_mark)) 
        for _str in map(str.strip, sys.stdin) 
            for _name, _mark in [_str.split()]
)
# print(_tuple) # test

_defaultdict = defaultdict(list)
[_defaultdict[_student.mark].append(_student.name) for _student in _tuple]
print(*sorted(_defaultdict.items(), key=lambda x: x[0])[1][1])