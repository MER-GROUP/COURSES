'''
Логическое выражение

Дано логическое выражение, состоящее из переменных, а также операторов |, &, and или or. 
Напишите программу, которая разбивает данную строку по указанным операторам.

Формат входных данных
На вход программе подается строка, содержащая логическое выражение, которое состоит из переменных 
и операторов |, &, and или or, между которыми могут располагаться пробелы.

Формат  выходных данных
Программа должна разбить введенную строку по указанным логическим операторам, захватывая 
вокруг стоящие пробелы, и вывести все значения, полученные при разбиении, через запятую и пробел.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/699083/tests_3181501.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.9/Module_11.9.11

Sample Input 1:
a and b or c
Sample Output 1:
a, b, c

Sample Input 2:
x   &   y   |   z
Sample Output 2:
x, y, z

Sample Input 3:
X&Y|Z&W
Sample Output 3:
X, Y, Z, W
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

def func(string: str) -> str:
    return re.split(
        pattern=rf'(?:\s*)(?:\||&|and|or)(?:\s*)',
        string=string,
        flags=re.MULTILINE
    )

if __name__ == '__main__':
    stdin = open(file='061-test.csv', mode='rt', encoding='utf-8', newline='')
    # sentense = map(str, stdin)
    sentense = stdin.read()
    print(sentense) # test
    print('------') # test
    pattern = rf''

    print(*func(sentense), sep=', ')