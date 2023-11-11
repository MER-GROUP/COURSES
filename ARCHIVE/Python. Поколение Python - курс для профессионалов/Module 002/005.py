'''
Функция convert()
Реализуйте функцию convert(), которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать строку string:

полностью в нижнем регистре, если букв в нижнем регистре 
в этой строке больше
полностью в верхнем регистре, если букв в верхнем 
регистре в этой строке больше
полностью в нижнем регистре, если количество букв 
в верхнем и нижнем регистрах в этой строке совпадает

Примечание 1. Символы строки, не являющиеся буквами, 
следует игнорировать.

Примечание 2. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию convert(), 
но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/569748/tests_2310060.zip

Sample Input 1:
print(convert('BEEgeek'))
Sample Output 1:
beegeek

Sample Input 2:
print(convert('pyTHON'))
Sample Output 2:
PYTHON

Sample Input 3:
print(convert('pi31415!'))
Sample Output 3:
pi31415!
'''
def convert(s: str) -> str:
    from string import ascii_lowercase, ascii_uppercase
    big, small = 0, 0
    for c in s:
        if c in ascii_lowercase: small += 1
        elif c in ascii_uppercase: big += 1
    return s.lower() if small >= big else s.upper()

if __name__ == '__main__':
    print(convert('BEEgeek'))
    print(convert('pyTHON'))
    print(convert('pi31415!'))