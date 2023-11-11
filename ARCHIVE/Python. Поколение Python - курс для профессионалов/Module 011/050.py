'''
Функция abbreviate()

Аббревиатура — слово, образованное сокращением слова или словосочетания и читаемое 
по алфавитному названию начальных букв или по начальным звукам слов, входящих в него.

Реализуйте функцию abbreviate(), которая принимает один аргумент:

phrase — фраза

Функция должна создавать из фразы phrase аббревиатуру в верхнем регистре и возвращать её.

Примечание 1. В аббревиатуре должны присутствовать как начальные буквы слов, 
так и начальные буквы подслов, начинающихся с заглавной буквы, например, 
JavaScript Object Notation -> JSON.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию abbreviate(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680265/tests_2898549.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.7/Module_11.7.15

Sample Input 1:
print(abbreviate('javaScript object notation'))
Sample Output 1:
JSON

Sample Input 2:
print(abbreviate('frequently asked questions'))
Sample Output 2:
FAQ

Sample Input 3:
print(abbreviate('JS game sec'))
Sample Output 3:
JSGS
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

def abbreviate(_str: str) -> str:
    arr = _str.split()
    print(arr)
    abr = ''
    pattern = rf'[A-Z]'
    for s in arr:
        abr += s[0].upper()
        match = re.findall(pattern, s[1:])
        if match:
            abr += ''.join(match)
    return abr

if __name__ == '__main__':
    stdin = open(file='050-test.csv', mode='rt', encoding='utf-8', newline='')
    words = map(str.strip, stdin)
    # print(*words) # test
    # pattern = rf''

    print(abbreviate(*words))