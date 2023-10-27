'''
Первые буквы

Напишите программу, которая меняет местами первые две буквы в каждом слове, 
состоящем из двух или более букв.

Формат входных данных
На вход программе подается строка, содержащая слова.

Формат выходных данных
Программа должна в введенной строке заменить первые две буквы в каждом слове, 
состоящем из двух или более букв, и вывести полученный результат.

Примечание 1. Словом будем считать последовательность символов, 
соответствующих \w, окруженную символами, соответствующими \W.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680266/tests_2902179.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.8/Module_11.8.12

Sample Input 1:
This is Python
Sample Output 1:
hTis si yPthon

Sample Input 2:
Hi, everyone. Lets start a lesson!
Sample Output 2:
iH, veeryone. eLts tsart a elsson!
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

def normalize_whitespace(string: str) -> str:
    return re.sub(
        pattern=rf'\b(\w)(\w)(\w*)',
        repl=r'\g<2>\g<1>\g<3>',
        string=string
    )

if __name__ == '__main__':
    stdin = open(file='056-test.csv', mode='rt', encoding='utf-8', newline='')
    # sentense = map(str, stdin)
    sentense = stdin.read()
    print(sentense) # test
    print('------') # test
    pattern = rf''

    print(normalize_whitespace(sentense))