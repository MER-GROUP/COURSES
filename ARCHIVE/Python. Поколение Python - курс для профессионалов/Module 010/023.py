'''
Функция simple_sequence()
Реализуйте генераторную функцию simple_sequence(), которая не принимает 
никаких аргументов.

Функция должна возвращать генератор, порождающий бесконечную возрастающую 
последовательность натуральных чисел, в которой каждое число встречается столько раз, 
каково оно:

1, 2, 2, 3, 3, 3, 4, 4, 4, 4, ..

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую 
генераторную функцию simple_sequence(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640048/tests_2777710.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.5/Module_10.5.15

Sample Input 1:
generator = simple_sequence()
print(next(generator))
print(next(generator))
Sample Output 1:
1
2

Sample Input 2:
generator = simple_sequence()
numbers = [next(generator) for _ in range(10)]
print(*numbers)
Sample Output 2:
1 2 2 3 3 3 4 4 4 4
'''
from __future__ import annotations
from _collections_abc import Generator

def simple_sequence() -> Generator:
    index = 1
    while True:
        for _ in range(index):
            yield index
        index += 1

if __name__ == '__main__':
    generator = simple_sequence()
    print(next(generator))
    print(next(generator))

    generator = simple_sequence()
    numbers = [next(generator) for _ in range(10)]
    print(*numbers)