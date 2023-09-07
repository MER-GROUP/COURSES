'''
Функция password_gen()
Вам доступна функция password_gen(), которая возвращает генератор, порождающий все трехсимвольные строковые пароли в порядке возрастания, составленные из цифр от 
0
0 до 
9
9 включительно.

Перепишите данную функцию с использованием функции product(), чтобы она выполняла ту же задачу.

Примечание. В тестирующую систему сдайте программу, содержащую только необходимую функцию password_gen(), но не код, вызывающий ее.

def password_gen():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                yield str(i) + str(j) + str(k)
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
import itertools as it

def password_gen():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                yield str(i) + str(j) + str(k)

if __name__ == '__main__':
    pass