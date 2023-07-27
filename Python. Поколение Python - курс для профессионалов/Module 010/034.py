'''
Функция count_iterable()
Реализуйте функцию count_iterable() с использованием генераторных выражений, 
которая принимает один аргумент:

iterable — итерируемый объект
Функция должна возвращать единственное число — количество элементов итерируемого объекта iterable.

Примечание 1. Гарантируется, что передаваемый в функцию итерируемый объект является конечным.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию count_iterable(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640049/tests_2780212.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.6/Module_10.6.17

Sample Input 1:
print(count_iterable([1, 2, 3, 4, 5]))
Sample Output 1:
5

Sample Input 2:
numbers = iter([1, 2, 3, 4, 5, 6, 7])
print(count_iterable(numbers))
Sample Output 2:
7

Sample Input 3:
data = tuple(range(432, 3845, 17))
print(count_iterable(data))
Sample Output 3:
201
'''
from __future__ import annotations
from _collections_abc import Generator, Iterable, Iterator

def count_iterable(iterable: Iterable) -> int:
    if isinstance(iterable, (Iterator, Generator)):
        return sum(1 for _ in iterable)
    return len(iterable)
            
if __name__ == '__main__':
    print(count_iterable([1, 2, 3, 4, 5]))

    numbers = iter([1, 2, 3, 4, 5, 6, 7])
    print(count_iterable(numbers))

    data = tuple(range(432, 3845, 17))
    print(count_iterable(data))