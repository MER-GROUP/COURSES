'''
Функция max_pair()

Реализуйте функцию max_pair(), которая принимает один аргумент:

iterable — итерируемый объект, элементами которого являются числа

Функция должна возвращать единственное число — максимальную сумму двух соседних 
чисел итерируемого объекта iterable.

Примечание 1. Рассмотрим список чисел 1, 8, 2, 4, 3 из первого теста. Из данной 
последовательности можно получить следующие пары соседних элементов: 1 и 8, 8 и 2, 2 и 4, 4 и 3. 
Максимальную сумму имеет вторая пара — 10.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является 
множеством, а также содержит не менее двух элементов.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию max_pair(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/674263/tests_2798508.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.10/Module_10.10.15

Sample Input 1:
print(max_pair([1, 8, 2, 4, 3]))
Sample Output 1:
10

Sample Input 2:
iterator = iter([1, 2, 3, 4, 5])
print(max_pair(iterator))
Sample Output 2:
9

Sample Input 3:
iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])
print(max_pair(iterator))
Sample Output 3:
0
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
import itertools as it

def max_pair(iterable: Iterable) -> int|float:
    return sum(
        max(
            it.pairwise(iterable),
            key=sum
        )
    )

if __name__ == '__main__':
    print(max_pair([1, 8, 2, 4, 3]))

    iterator = iter([1, 2, 3, 4, 5])
    print(max_pair(iterator))

    iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])
    print(max_pair(iterator))