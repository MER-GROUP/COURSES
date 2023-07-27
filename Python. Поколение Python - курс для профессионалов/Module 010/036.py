'''
Функция interleave()
Реализуйте функцию interleave() с использованием генераторных выражений, которая 
принимает произвольное количество позиционных аргументов, каждый из которых 
является последовательностью.

Функция должна возвращать генератор, порождающий каждый элемент всех переданных 
последовательностей: сначала первый элемент первой последовательности, затем первый 
элемент второй последовательности, и так далее; после второй элемент первой 
последовательности, затем второй элемент второй последовательности, и так далее.

Примечание 1. Последовательностью является коллекция, поддерживающая индексацию 
и имеющая длину. Например, объекты типа list, str, tuple являются последовательностями.

Примечание 2. Гарантируется, что все последовательности, передаваемые в функцию, 
имеют равные длины.

Примечание 3. Гарантируется, что в функцию всегда подается хотя бы одна последовательность.

Примечание 4. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию interleave(), но не код, вызывающий ее.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640049/tests_2780215.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.6/Module_10.6.19

Sample Input 1:
print(*interleave('bee', '123'))
Sample Output 1:
b 1 e 2 e 3

Sample Input 2
numbers = [1, 2, 3]
squares = [1, 4, 9]
qubes = [1, 8, 27]
print(*interleave(numbers, squares, qubes))
Sample Output 2:
1 1 1 2 4 8 3 9 27
'''
from __future__ import annotations
from _collections_abc import Generator, Iterable, Iterator

"""
Для разных длин
"""
# from itertools import zip_longest
# def interleave(*args) -> Generator:
#     return (j for i in zip_longest(*args) for j in i)

# def interleave(*args) -> Generator:
#     arr_iterators = list()
#     for el in args:
#         arr_iterators.append(iter(el))

#     while arr_iterators:
#         try:
#             for it in arr_iterators:
#                 yield next(it)
#         except StopIteration:
#             arr_iterators.remove(it)

"""
Для одинаковых длин
"""
# def interleave(*args) -> Generator:
#     return (j for i in zip(*args) for j in i)

def interleave(*args) -> Generator:
    arr_iterators = list()
    for el in args:
        arr_iterators.append(iter(el))

    while True:
        try:
            for it in arr_iterators:
                yield next(it)
        except StopIteration:
            break
            
if __name__ == '__main__':
    # 1
    print(*interleave('bee', '123'))

    # 2
    numbers = [1, 2, 3]
    squares = [1, 4, 9]
    qubes = [1, 8, 27]
    print(*interleave(numbers, squares, qubes))

    # 3
    numbers1 = tuple(range(1, 10))
    numbers2 = list(range(10, 20))
    numbers3 = tuple(range(20, 30))
    numbers4 = tuple(range(30, 40))
    print(*interleave(numbers1, numbers2, numbers3, numbers4))
    
    # 5
    numbers1 = tuple(range(38, 99, 7))
    numbers2 = tuple(range(65, 113, 9))
    string1 = 'BEEGEEKbeegeek'
    string2 = 'STEPIKstepik'
    numbers3 = list(range(1, 77, 19))
    numbers4 = list(range(2, 78, 20))
    print(*interleave(numbers3, string2, numbers4, string1, numbers2, numbers1))