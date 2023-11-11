'''
Функция is_rising()

Реализуйте функцию is_rising(), которая принимает один аргумент:

iterable — итерируемый объект, элементами которого являются числа

Функция должна возвращать True, если элементы итерируемого объекта 
расположены строго по возрастанию, или False в противном случае.

Примечание 1. Гарантируется, что итерируемый объект, передаваемый 
в функцию, не является множеством, а также содержит не менее двух элементов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию is_rising(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/674263/tests_3154353.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.10/Module_10.10.14

Sample Input 1:
print(is_rising([1, 2, 3, 4, 5]))
Sample Output 1:
True

Sample Input 2:
iterator = iter([1, 1, 1, 2, 3, 4])
print(is_rising(iterator))
Sample Output 2:
False

Sample Input 3:
iterator = iter(list(range(100, 200)))
print(is_rising(iterator))
Sample Output 3:
True
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
import itertools as it

def is_rising(iterable: Iterable) -> bool:
    return all(
                map(
                    lambda x: x[0] < x[1],
                    it.pairwise(
                        iterable
                    )
            )
        )

if __name__ == '__main__':
    print(is_rising([1, 2, 3, 4, 5]))

    iterator = iter([1, 1, 1, 2, 3, 4])
    print(is_rising(iterator))

    iterator = iter(list(range(100, 200)))
    print(is_rising(iterator))