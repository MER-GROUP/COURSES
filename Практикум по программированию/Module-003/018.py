'''
Шифр Юлия
Юлий Цезарь использовал свой способ шифрования текста. 
Каждая буква заменялась на следующую по алфавиту 
через K позиций по кругу. Необходимо по заданной шифровке 
определить исходный текст.

Входные данные
В первой строке дана шифровка, состоящая из заглавных латинских букв. 
Во второй строке число K (1 ≤ K ≤ 10).

Выходные данные
Требуется вывести результат расшифровки.

Sample Input 1:
XPSE
1
Sample Output 1:
WORD

Sample Input 2:
ZABC
3
Sample Output 2:
WXYZ
'''
import sys

def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

# sys.stdin = open(file='018.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(
    map(
        lambda x: int(x) if is_int(x) else x.strip(),
        sys.stdin
    )
)
# print(arr) # test

for c in arr[0]:
    if ord(c) - arr[1] >= ord('A'):
        print(chr(ord(c) - arr[1]), end='')
    else:
        print(chr((ord('Z') + 1) - (ord('A') - (ord(c) - arr[1]))), end='')
print()