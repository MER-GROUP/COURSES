'''
Функция palindromes()
Реализуйте генераторную функцию palindromes(), которая не принимает никаких аргументов.

Функция должна возвращать генератор, порождающий бесконечную последовательность натуральных 
чисел-палиндромов.

Примечание 1. Число-палиндром — число, которое читается одинаково как справа налево, 
так и слева направо.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую 
генераторную функцию palindromes(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640048/tests_3139059.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.5/Module_10.5.26

Sample Input 1:
generator = palindromes()
print(next(generator))
print(next(generator))
print(next(generator))
Sample Output 1:
1
2
3

Sample Input 2:
generator = palindromes()
numbers = [next(generator) for _ in range(30)]
print(*numbers)
Sample Output 2:
1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191 202 212
'''

from __future__ import annotations
from _collections_abc import Generator

def palindromes() -> Generator:
    def is_palindrom(n: int) -> bool:
        return (False, True)[str(n) ==str(n)[::-1]]
    
    n = 1
    while True:
        if is_palindrom(n):
            yield n
        n += 1
            
if __name__ == '__main__':
    generator = palindromes()
    print(next(generator))
    print(next(generator))
    print(next(generator))

    generator = palindromes()
    numbers = [next(generator) for _ in range(30)]
    print(*numbers)