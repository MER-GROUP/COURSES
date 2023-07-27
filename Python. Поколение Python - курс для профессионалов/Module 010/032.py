'''
Функция cubes_of_odds()
Вам доступна генераторная функция cubes_of_odds(), принимающая в качестве аргумента итерируемый объект, элементами которого являются целые числа, и возвращающая генератор, порождающий последовательность нечетных чисел переданного итерируемого объекта, возведенных в третью степень.

Перепишите данную функцию с использованием генераторного выражения, чтобы она выполняла ту же задачу.

Примечание 1. Если генераторное выражение становится достаточно большим, его можно записать в виде нескольких строк.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию cubes_of_odds(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640049/tests_2780213.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.6/Module_10.6.15

def cubes_of_odds(iterable):
    for number in iterable:
        if number % 2:
            yield number ** 3

Sample Input 1:
print(*cubes_of_odds([1, 2, 3, 4, 5]))
Sample Output 1:
1 27 125

Sample Input 2:
evens = [2, 4, 6, 8, 10]
print(list(cubes_of_odds(evens)))
Sample Output 2:
[]
'''
from __future__ import annotations
from _collections_abc import Generator

def cubes_of_odds(iterable) -> Generator:
    # for number in iterable:
    #     if number % 2:
    #         yield number ** 3
    return (number ** 3 for number in iterable if number % 2)
            
if __name__ == '__main__':
    print(*cubes_of_odds([1, 2, 3, 4, 5]))

    evens = [2, 4, 6, 8, 10]
    print(list(cubes_of_odds(evens)))