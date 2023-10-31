'''
Повторяющиеся слова 🌶️

Напишите программу, которая заменяет все повторяющиеся рядом стоящие слова на одно слово.

Формат входных данных
На вход программе подается строка, содержащая слова.

Формат выходных данных
Программа должна в введенной строке заменить все повторяющиеся рядом стоящие слова 
на одно слово и вывести полученный результат.

Примечание 1. Программа должна быть чувствительной к регистру, то есть, например, 
слова python и Python считаются различными.

Примечание 2. Словом будем считать последовательность символов, соответствующих \w, 
окруженную символами, соответствующими \W.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680266/tests_2907191.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.8/Module_11.8.14

Sample Input 1:
beegeek,beegeek,beegeek! python python.. Python.. stepik?stepik?stepik
Sample Output 1:
beegeek! python.. Python.. stepik

Sample Input 2:
hi, hi, hi, hello, hello, HELLO, HELLO, HELLO, HELLO, hello!
Sample Output 2:
hi, hello, HELLO, hello!

Sample Input 3:
wow Wow wow WOW
Sample Output 3:
wow Wow wow WOW
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

def func(string: str) -> str:
    # pattern = rf'\b(\w+)(\W\1\b)+'
    pattern = rf'\b(\w+)(\W+\1\b)+'
    repls = map(lambda x: x[1], re.findall(pattern, string))
    # print(*repls) # test #
    for repl in repls:
        string = re.sub(pattern, rf'\g<1>', string)
    return string


if __name__ == '__main__':
    stdin = open(file='058-test.csv', mode='rt', encoding='utf-8', newline='')
    # sentense = map(str, stdin)
    sentense = stdin.read()
    print(sentense) # test
    print('------') # test
    pattern = rf''

    print(func(sentense))