'''
Функция password_gen()
Вам доступна функция password_gen(), которая возвращает генератор, 
порождающий все трехсимвольные строковые пароли в порядке возрастания, 
составленные из цифр от 0 до 9 включительно.

Перепишите данную функцию с использованием функции product(), 
чтобы она выполняла ту же задачу.

Примечание. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию password_gen(), но не код, вызывающий ее.

def password_gen():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                yield str(i) + str(j) + str(k)

Sample Input:
passwords = password_gen()
print(next(passwords))
print(next(passwords))
print(next(passwords))

Sample Output:
000
001
002
'''
from __future__ import annotations
from _collections_abc import Generator, Iterator, Iterable, Callable
import itertools as it

# def password_gen():
#     for i in range(10):
#         for j in range(10):
#             for k in range(10):
#                 yield str(i) + str(j) + str(k)

def password_gen():
    for i, j, k in it.product(range(10), range(10), range(10)):
                yield str(i) + str(j) + str(k)

if __name__ == '__main__':
    passwords = password_gen()
    print(next(passwords))
    print(next(passwords))
    print(next(passwords))