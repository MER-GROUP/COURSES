'''
Онлайн-школа BEEGEEK

В онлайн-школе BEEGEEK логин учетной записи определяется следующим образом:

первым символом является символ нижнего подчеркивания _
затем следуют одна или более цифр
после записываются ноль или более латинских букв в произвольном регистре
логин может иметь на конце необязательный символ нижнего подчеркивания _

Напишите программу, которая принимает произвольное количество строк и определяет, 
какие из них представляют собой корректный логин онлайн-школы BEEGEEK.

Формат входных данных
На вход программе подаётся произвольное количество строк, каждая из которых содержит 
набор произвольных символов.

Формат выходных данных
Программа должна для каждой введенной строки вывести True, если она представляет 
собой корректный логин онлайн-школы BEEGEEK, или False в противном случае.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680263/tests_2823646.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.6/Module_11.6.10

Sample Input 1:
_123abc_
_1abc_
123abc
_abc123
_123abc__
Sample Output 1:
True
True
False
False
False

Sample Input 2:
_1
_1_
Sample Output 2:
True
True
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

if __name__ == '__main__':
    stdin = open(file='039-test.csv', mode='rt', encoding='utf-8', newline='')
    pattern = r'^_' +\
                r'\d+' +\
                r'[a-zA-Z]*' +\
                r'_?$'
    
    for password in map(str.strip, stdin):
        # print(password) # test
        match = re.fullmatch(pattern, password)
        if match:
            print('True')
        else:
            print('False')