'''
Точка с запятой

Напишите программу, которая разбивает строку по символам точки, запятой и точки с запятой.

Формат входных данных
На вход программе подается строка, содержащая различные значения, 
разделенные символами точки ., запятой , или точки с запятой ;, 
вокруг которых могут располагаться пробелы.

Формат выходных данных
Программа должна разбить введенную строку по символам точки, запятой и точки с запятой, 
захватывая вокруг стоящие пробелы, и вывести все значения, полученные при разбиении, 
через пробел.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/699083/tests_3181502.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.9/Module_11.9.10

Sample Input 1:
bee,geek . Python   ,  C++
Sample Output 1:
bee geek Python C++

Sample Input 2:
py py; hi  hi; go-go-go
Sample Output 2:
py py hi  hi go-go-go

Sample Input 3:
arthur;timur,dima.anri
Sample Output 3:
arthur timur dima anri
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

def func(string: str) -> str:
    return re.split(
        rf'\s*[.,;]\s*',
        string,
        re.MULTILINE
    )

if __name__ == '__main__':
    stdin = open(file='060-test.csv', mode='rt', encoding='utf-8', newline='')
    # sentense = map(str, stdin)
    sentense = stdin.read()
    print(sentense) # test
    print('------') # test
    pattern = rf''

    print(*func(sentense))