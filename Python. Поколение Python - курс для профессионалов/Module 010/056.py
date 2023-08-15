'''
Функция take()

Реализуйте функцию take(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
n — натуральное число

Функция должна возвращать итератор, генерирующей последовательность из первых n элементов 
итерируемого объекта iterable.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны располагаться 
в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию take(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/666563/tests_2788764.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.9/Module_10.9.15

Sample Input 1:
print(*take(range(10), 5))
Sample Output 1:
0 1 2 3 4

Sample Input 2:
iterator = iter('beegeek')
print(*take(iterator, 22))
Sample Output 2:
b e e g e e k

Sample Input 3:
iterator = iter('beegeek')
print(*take(iterator, 1))
Sample Output 3:
b
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
import itertools as it

# def take(iterable: Iterable, n: int) -> Iterator|Generator:
#     return it.compress(
#         iterable,
#         range(1, n+1)
#     )

from itertools import islice as take

if __name__ == '__main__':
    print(*take(range(10), 5))

    iterator = iter('beegeek')
    print(*take(iterator, 22))

    iterator = iter('beegeek')
    print(*take(iterator, 1))