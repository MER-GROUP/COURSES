'''
Функция first_largest()

Реализуйте функцию first_largest(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект, элементами которого являются целые числа
number — произвольное число

Функция должна возвращать индекс первого элемента итерируемого объекта iterable, 
который больше number. Если таких элементов нет, функция должна вернуть число -1.

Примечание 1. Рассмотрим список чисел 10, 2, 14, 7, 7, 18, 20 из первого теста. 
Первым числом, превосходящим 11, является число 14, которое имеет индекс 2.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, 
не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию first_largest(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/666563/tests_2788763.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.9/Module_10.9.17

Sample Input 1:
numbers = [10, 2, 14, 7, 7, 18, 20]
print(first_largest(numbers, 11))
Sample Output 1:
2

Sample Input 2:
iterator = iter([-1, -2, -3, -4, -5])
print(first_largest(iterator, 10))
Sample Output 2:
-1

Sample Input 3:
iterator = iter([18, 21, 14, 72, 73, 18, 20])
print(first_largest(iterator, 10))
Sample Output 3:
0
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
import itertools as it

def first_largest(iterable: Iterable, number: int) -> int:
    return next(
        it.dropwhile(
            lambda x: number >= x[1],
            enumerate(iterable)
        ),
        [-1]
    )[0]

if __name__ == '__main__':
    numbers = [10, 2, 14, 7, 7, 18, 20]
    print(first_largest(numbers, 11))

    iterator = iter([-1, -2, -3, -4, -5])
    print(first_largest(iterator, 10))

    iterator = iter([18, 21, 14, 72, 73, 18, 20])
    print(first_largest(iterator, 10))