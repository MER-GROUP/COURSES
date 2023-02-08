'''
Изменить регистр символа

Измените регистр символа, если он был латинской буквой: 
сделайте его заглавным, если он был строчной буквой и наоборот. 

Любой другой символ выведите как есть, ничего не меняя.

Входные данные
Задан единственный символ C.

Выходные данные
Необходимо вывести  получившийся символ.

Sample Input 1:
V
Sample Output 1:
v

Sample Input 2:
a
Sample Output 2:
A
'''
import sys
from string import ascii_letters as ascii

# sys.stdin = open(file='009.csv', mode='rt', encoding='utf-8', newline='')
c = sys.stdin.read()

print((c.upper(), c.lower())['A' <= c <= 'Z'] if c in ascii else c)