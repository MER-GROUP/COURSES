'''
Функция drop_this()

Реализуйте функцию drop_this(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
obj — произвольный объект

Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого 
объекта iterable, начиная с элемента, не равного obj.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны 
располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является 
множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию drop_this(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/666563/tests_3152982.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.9/Module_10.9.13

Sample Input 1:
numbers = [0, 0, 0, 1, 2, 3]
print(*drop_this(numbers, 0))
Sample Output 1:
1 2 3

Sample Input 2:
iterator = iter('bbbbeebee')
print(*drop_this(iterator, 'b'))
Sample Output 2:
e e b e e

Sample Input 3:
iterator = iter('ssssssssssssssssssssssss')
print(list(drop_this(iterator, 's')))
Sample Output 3:
[]
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
import itertools as it

drop_this = lambda iterable, obj: it.dropwhile(
    lambda x: x == obj,
    iterable
)

if __name__ == '__main__':
    numbers = [0, 0, 0, 1, 2, 3]
    print(*drop_this(numbers, 0))

    iterator = iter('bbbbeebee')
    print(*drop_this(iterator, 'b'))

    iterator = iter('ssssssssssssssssssssssss')
    print(list(drop_this(iterator, 's')))