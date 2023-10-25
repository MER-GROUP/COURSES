'''
Функция normalize_jpeg()

Реализуйте функцию normalize_jpeg(), которая принимает один аргумент:

filename — название файла, имеющее расширение jpeg или jpg, которое может быть 
записано буквами произвольного регистра

Функция должна возвращать новое название файла с нормализованным расширением — jpg.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию normalize_jpeg(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680266/tests_2902180.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.8/Module_11.8.9

Sample Input 1:
print(normalize_jpeg('stepik.jPeG'))
Sample Output 1:
stepik.jpg

Sample Input 2:
print(normalize_jpeg('mountains.JPG'))
Sample Output 2:
mountains.jpg

Sample Input 3:
print(normalize_jpeg('windows11.jpg'))
Sample Output 3:
windows11.jpg
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin
# from collections import defaultdict

def normalize_jpeg(filename: str) -> str:
    return re.sub(r'((jpeg)|(jpg))$', r'jpg', filename, flags=re.IGNORECASE)

if __name__ == '__main__':
    stdin = open(file='053-test.csv', mode='rt', encoding='utf-8', newline='')
    # sentense = map(str.strip, stdin)
    sentense = stdin.read()
    print(sentense) # test
    print('------') # test
    pattern = rf''

    print(normalize_jpeg(sentense))