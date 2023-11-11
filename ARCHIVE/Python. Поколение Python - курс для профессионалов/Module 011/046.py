'''
Подслова

Напишите программу, которая принимает на вход строку текста и некоторое 
слово и определяет, сколько раз данное слово встречается как подслово в введенном тексте.

Формат входных данных
На вход программе на первой строке подается текст, на второй — слово.

Формат выходных данных
Программа должна определить, сколько раз данное слово встречается как подслово 
в введенном тексте, и вывести полученный результат.

Примечание 1. Словом будем считать последовательность символов, соответствующих \w, 
окруженную символами, соответствующими \W. Подсловом же будет являться последовательность 
символов, соответствующих \w, окруженную символами, соответствующими \w. 
Например, is является подсловом optimist, а age не является подсловом ageless.

Примечание 2. Программа должна учитывать регистр. То есть, например, 
слова Python и python считаются разными.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680265/tests_2830471.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.7/Module_11.7.11

Sample Input 1:
existing pessimist optimist this is
is
Sample Output 1:
3

Sample Input 2:
I love Python very much, what about me hahah
ha
Sample Output 2:
2

Sample Input 3:
thdbakru rubabadjso babadirnid iehedba  ibebibeb duabafbf
ba
Sample Output 3:
5
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

if __name__ == '__main__':
    stdin = open(file='046-test.csv', mode='rt', encoding='utf-8', newline='')
    text, word = map(str.strip, stdin)
    # print(text, word, sep='\n') # test
    pattern = rf'\B{word}\B'

    print(
        len(
            re.findall(
                pattern,
                text
            )
        )
    )