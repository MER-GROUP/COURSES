'''
Функция all_together()
Реализуйте функцию all_together() с использованием генераторных выражений, 
которая принимает произвольное количество позиционных аргументов, каждый из которых 
является итерируемым объектом.

Функция должна возвращать генератор, порождающий каждый элемент всех переданных 
итерируемых объектов: сначала все элементы первого итерируемого объекта, затем второго, и так далее.

Примечание 1. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию all_together(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640049/tests_2780217.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.6/Module_10.6.18

Sample Input 1:
objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]
print(*all_together(*objects))
Sample Output 1:
0 1 2 b e e 1 3 5 2 4 6

Sample Input 2:
objects = [[1, 2, 3], [(0, 0), (1, 1)], {'geek': 1}]
print(*all_together(*objects))
Sample Output 2:
1 2 3 (0, 0) (1, 1) geek

Sample Input 3:
print(list(all_together()))
Sample Output 3:
[]
'''
from __future__ import annotations
from _collections_abc import Generator, Iterable, Iterator

def all_together(*args) -> Generator:
    yield from (j for i in args for j in i)
            
if __name__ == '__main__':
    objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]
    print(*all_together(*objects))

    objects = [[1, 2, 3], [(0, 0), (1, 1)], {'geek': 1}]
    print(*all_together(*objects))

    print(list(all_together()))