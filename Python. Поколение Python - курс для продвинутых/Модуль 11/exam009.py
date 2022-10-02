'''
Напишите функцию call(), которая принимает произвольную функцию и 
аргументы для неё и делает вызов переданной функции, возвращая ее значение.

Примечание 1. Приведенный ниже код, при условии, 
что функция call() написана правильно

def mul7(x):
    return x * 7

def add2(x, y):
    return x + y

def add3(x, y, z):
    return x + y + z

print(call(mul7, 10))
print(call(add2, 2, 7))
print(call(add3, 10, 30, 40))
print(call(bool, 0))

должен выводить:
70
9
80
False

Примечание 2. Вызывать функцию call() не нужно, требуется только реализовать ее.
'''
# Решение
def mul7(x):
    return x * 7

def add2(x, y):
    return x + y

def add3(x, y, z):
    return x + y + z

def call(f1, *args):
    return f1(*args)

print(call(mul7, 10))
print(call(add2, 2, 7))
print(call(add3, 10, 30, 40))
print(call(bool, 0))