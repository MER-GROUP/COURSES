'''
Функция factorials()
Реализуйте функцию factorials() с использованием функции accumulate(), 
которая принимает один аргумент:

n — натуральное число

Функция должна возвращать итератор, генерирующий последовательность из n чисел, 
каждое из которых является факториалом очередного натурального числа.

Примечание 1. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию factorials(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640045/tests_3150848.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.8/Module_10.8.16

Sample Input 1:
numbers = factorials(6)
print(*numbers)
Sample Output 1:
1 2 6 24 120 720

Sample Input 2:
numbers = factorials(2)
print(next(numbers))
print(next(numbers))
Sample Output 2:
1
2
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
from itertools import count

pass

if __name__ == '__main__':
    pass