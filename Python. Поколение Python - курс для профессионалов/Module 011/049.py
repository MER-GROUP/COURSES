'''
Одинаковые и разные ☕️

В одной из предыдущих задач мы уже наблюдали различие в написании Британских и Американских слов. 
Еще одно различие заключается в том, что Британия сохранила использование сочетания 
букв our в своих словах, в то время как Америка отказалась от буквы u и использует лишь or.

Напишите программу, которая определяет, сколько раз слово встречается в тексте, 
учитывая его Британско-Американское написание.

Формат входных данных
На вход программе на первой строке подается слово, которое записано в Британском варианте, 
а на следующей — текст.

Формат выходных данных
Программа должна определить, сколько раз введенное слово встречается в тексте, 
учитывая его Британско-Американское написание, и вывести полученный результат.

Примечание 1. Словом будем считать последовательность символов, соответствующих \w, 
окруженную символами, соответствующими \W.

Примечание 2. Гарантируется, что введенное слово состоит из 4 или более букв.

Примечание 3. Программа должна игнорировать регистр. То есть, например, 
слова Python и python считаются одинаковыми.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680265/tests_2898551.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.7/Module_11.7.14

Sample Input 1:
Odour
the odour coming out of the left over food was intolerable. Ammonia has a very pungent odor
Sample Output 1:
2

Sample Input 2:
hour
a lot of Hour or hor
Sample Output 2:
2
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

if __name__ == '__main__':
    stdin = open(file='049-test.csv', mode='rt', encoding='utf-8', newline='')
    word, text = map(str.strip, stdin)
    print(word, text, sep='\n') # test
    pattern = rf'\b{word[:-3]}o[u]?r\b'

    print(
        len(
            re.findall(
                pattern,
                text,
                re.IGNORECASE
            )
        )
    )