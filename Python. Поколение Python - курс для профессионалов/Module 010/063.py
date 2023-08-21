'''
Функция grouper()

Реализуйте функцию grouper(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
n — натуральное число

Функция должна возвращать итератор, генерирующий последовательность, элементами которой 
являются объединенные в кортежи по n элементов соседние элементы итерируемого объекта iterable. 
Если у элемента не достаточно соседей, то ими становится значение None.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией итераторе должны 
располагаться в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, 
не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию grouper(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/674263/tests_2788959.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.10/Module_10.10.17

Sample Input 1:
numbers = [1, 2, 3, 4, 5, 6]
print(*grouper(numbers, 2))
Sample Output 1:
(1, 2) (3, 4) (5, 6)

Sample Input 2:
iterator = iter([1, 2, 3, 4, 5, 6, 7])
print(*grouper(iterator, 3))
Sample Output 2:
(1, 2, 3) (4, 5, 6) (7, None, None)

Sample Input 3:
iterator = iter([1, 2, 3])
print(*grouper(iterator, 5))
Sample Output 3:
(1, 2, 3, None, None)
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
import itertools as it

def grouper(iterable: Iterable, n: int) -> Iterator|Generator:
    _iterable = iter(iterable)
    arr = list()
    while n:
        try:
            arr.append(next(_iterable))
            if n == len(arr):
                yield tuple(arr)
                arr.clear()
        except StopIteration:
            if arr:
                for _ in range(n-len(arr)):
                    arr.append(None)
                yield tuple(arr)
                arr.clear()
            return
    if arr:
        for _ in range(n-len(arr)):
            arr.append(None)
        yield tuple(arr)
        arr.clear()

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6]
    print(*grouper(numbers, 2))

    iterator = iter([1, 2, 3, 4, 5, 6, 7])
    print(*grouper(iterator, 3))

    iterator = iter([1, 2, 3])
    print(*grouper(iterator, 5))

    # -------------------------------------------
    def grouper(iterable, n):
        return it.repeat(iter(iterable), n)

    numbers = [1, 2, 3, 4, 5, 6]
    print(*grouper(numbers, 2))