'''
Функция drop_while_negative()

Реализуйте функцию drop_while_negative(), которая принимает один аргумент:

iterable — итерируемый объект, элементами которого являются целые числа

Функция должна возвращать итератор, генерирующий все числа итерируемого объекта iterable, 
начиная с первого неотрицательного числа.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны 
располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является 
множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию drop_while_negative(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/666563/tests_2796850.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.9/Module_10.9.12

Sample Input 1:
numbers = [-3, -2, -1, 0, 1, 2, 3]
print(*drop_while_negative(numbers))
Sample Output 1:
0 1 2 3

Sample Input 2:
iterator = iter([-3, -2, -1, 0, 1, 2, 3, -4, -5, -6])
print(*drop_while_negative(iterator))
Sample Output 2:
0 1 2 3 -4 -5 -6

Sample Input 3:
iterator = iter([-3, -2, -1, -4, -5, -6])
print(list(drop_while_negative(iterator)))
Sample Output 3:
[]
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
import itertools as it

def drop_while_negative(iterable: Iterable) -> Iterator|Generator:
    return it.dropwhile(
        lambda x: 0 > x, 
        iterable
    )

if __name__ == '__main__':
    numbers = [-3, -2, -1, 0, 1, 2, 3]
    print(*drop_while_negative(numbers))

    iterator = iter([-3, -2, -1, 0, 1, 2, 3, -4, -5, -6])
    print(*drop_while_negative(iterator))

    iterator = iter([-3, -2, -1, -4, -5, -6])
    print(list(drop_while_negative(iterator)))