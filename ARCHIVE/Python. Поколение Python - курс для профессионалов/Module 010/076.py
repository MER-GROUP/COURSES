'''
Системы счисления
Напишите программу, которая генерирует в системе счисления n все числа длины m.

Формат входных данных
На вход программе в первой строке подается натуральное число n≤16 — основание 
системы счисления, а затем натуральное число m — длина генерируемых чисел.

Формат выходных данных
Программа должна сгенерировать в системе счисления n все числа 
длины m и вывести их в порядке возрастания через пробел.

Примечание 1. В системах счислениях по основанию 11 и выше в качестве цифр 
должны использоваться заглавные латинские буквы:
A,B,C,D,...

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680669/tests_2817395.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.12/Module_10.12.22

Sample Input 1:
2
3
Sample Output 1:
000 001 010 011 100 101 110 111

Sample Input 2:
3
2
Sample Output 2:
00 01 02 10 11 12 20 21 22
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
import itertools as it
from string import digits, ascii_uppercase

def sytem_16(n: int, m: int) -> str:
    """
    Есть список, состоящий иp цифр (от 0 до 9) + заглавные латинские буквы. 
    Из данного списка нам нужно взять все значения до n (не включительно). 
    Потом к данному срезу применить функцию product, при этом repeat должно 
    быть равно m. После этого останется лишь правильно вывести всё это дело на экран. 
    """
    letters = digits + ascii_uppercase
    print(
        *map(
            ''.join,
            it.product(letters[:n], repeat=m)
        )
    )

if __name__ == '__main__':
    n, m = (int(input()) for i in range(2))
    sytem_16(n, m)