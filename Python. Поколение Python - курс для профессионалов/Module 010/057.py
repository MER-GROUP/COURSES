'''
Функция take_nth()

Реализуйте функцию take_nth(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
n — натуральное число

Функция должна возвращать n-ый по счету элемент итерируемого объекта iterable. 
Если итерируемый объект iterable содержит менее n элементов, функция должна вернуть значение None.

Примечание 1. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию take_nth(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/666563/tests_2788766.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.9/Module_10.9.16

Sample Input 1:
numbers = [11, 22, 33, 44, 55]
print(take_nth(numbers, 3))
Sample Output 1:
33

Sample Input 2:
iterator = iter('beegeek')
print(take_nth(iterator, 4))
Sample Output 2:
g

Sample Input 3:
iterator = iter('beegeek')
print(take_nth(iterator, 10))
Sample Output 3:
None
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
import itertools as it

def take_nth(iterable: Iterable, n: int) -> object:
    return next(    
        it.islice(
            iterable,
            n-1,
            n
        ),
        None
    )

if __name__ == '__main__':
    numbers = [11, 22, 33, 44, 55]
    print(take_nth(numbers, 3))

    iterator = iter('beegeek')
    print(take_nth(iterator, 4))

    iterator = iter('beegeek')
    print(take_nth(iterator, 10))