'''
Функция roundrobin() 🌶️
Реализуйте функцию roundrobin(), которая принимает произвольное количество позиционных аргументов, 
каждый из которых является итерируемым объектом.

Функция должна возвращать итератор, генерирующий последовательность из элементов всех переданных 
итерируемых объектов: сначала первый элемент первого итерируемого объекта, затем первый элемент 
второго итерируемого объекта, и так далее; после второй элемент первого итерируемого объекта, 
затем второй элемент второго итерируемого объекта, и так далее.

Примечание 1. Элементы итерируемых объектов в возвращаемом функцией итераторе должны располагаться 
в своем исходном порядке.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию roundrobin(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640045/tests_2789644.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.8/Module_10.8.18

Sample Input 1:
print(*roundrobin('abc', 'd', 'ef'))
Sample Output 1:
a d e b f c

Sample Input 2:
numbers = [1, 2, 3]
letters = iter('beegeek')
print(*roundrobin(numbers, letters))
Sample Output 2:
1 b 2 e 3 e g e e k

Sample Input 3:
print(list(roundrobin()))
Sample Output 3:
[]
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
from itertools import count, accumulate, cycle, starmap, zip_longest

def roundrobin(*args) -> Iterator|Generator:
    if args:
        for i in zip_longest(*args, fillvalue=float('inf')):
            yield from (j for j in i if not j == float('inf'))
    else:
        return iter(args)

# def take(iterable, n):
#     for elem, _ in zip(iterable, range(n)):
#         yield elem

# def roundrobin(*iterables):
#     non_empty = len(iterables)
#     iterables = cycle(map(iter, iterables))
#     while non_empty:
#         try:
#             for it in iterables:
#                 yield next(it)
#         except StopIteration:
#             non_empty -= 1
#             iterables = cycle(take(iterables, non_empty))

if __name__ == '__main__':
    # 1
    print(*roundrobin('abc', 'd', 'ef'))
    # 2
    numbers = [1, 2, 3]
    letters = iter('beegeek')
    print(*roundrobin(numbers, letters))
    # 3
    print(list(roundrobin()))
    # 4
    numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers2 = range(5)
    letters = iter('beegeek')
    print(*roundrobin(numbers1, numbers2, letters))
    # >>> 1 0 b 2 1 e 3 2 e 4 3 g 5 4 e 6 e 7 k 8 9 10
    # 9
    numbers = iter([1, 2, 3])
    nones = iter([None, None, None, None])
    print(*roundrobin(numbers, nones))
    # >>> 1 None 2 None 3 None None
    # my
    numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers2 = []
    letters = iter('beegeek')
    print(*roundrobin(numbers1, numbers2, letters))
    # >>> 1 None 2 None 3 None None