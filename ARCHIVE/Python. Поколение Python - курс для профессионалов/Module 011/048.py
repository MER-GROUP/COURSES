'''
Одинаковые и разные 🍕

Американский английский и Британский английский языки имеют несколько различий, 
одно из которых наблюдается в написании слов. Например, слова, написанные 
на Американском английском языке и имеющие суффикс ze, в Британском варианте 
языка часто записываются с использованием суффикса se. 

Напишите программу, которая определяет, сколько раз слово встречается в тексте, 
учитывая его Британско-Американское написание.

Формат входных данных
На вход программе на первой строке подается слово, которое может быть записано 
как в Британском, так в Американском варианте, а на следующей — текст.

Формат выходных данных
Программа должна определить, сколько раз введенное слово встречается в тексте, 
учитывая его Британско-Американское написание, и вывести полученный результат.

Примечание 1. Словом будем считать последовательность символов, 
соответствующих \w, окруженную символами, соответствующими \W.

Примечание 2. Программа должна игнорировать регистр. То есть, 
например, слова Python и python считаются одинаковыми.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680265/tests_2898553.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.7/Module_11.7.13

Sample Input 1:
Familiarize
stepik has such a good ui that it takes no time to familiarise its environment. To familiarize oneself with ui of stepik is easy
Sample Output 1:
2

Sample Input 2:
Gseze
Gzeze Gsese Gseze Gzese
Sample Output 2:
2
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

if __name__ == '__main__':
    stdin = open(file='048-test.csv', mode='rt', encoding='utf-8', newline='')
    word, text = map(str.strip, stdin)
    print(word, text, sep='\n') # test
    pattern = rf'\b{word[:-2]}[sz]e\b'

    print(
        len(
            re.findall(
                pattern,
                text,
                re.IGNORECASE
            )
        )
    )