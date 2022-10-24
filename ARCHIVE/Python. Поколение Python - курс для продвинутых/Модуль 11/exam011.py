'''
Напишите функцию arithmetic_operation(), 
которая принимает символ одной из четырех арифметических 
операций (+, -, *, /) и возвращает функцию двух 
аргументов для соответствующей операции.

Примечание 1. Приведенный ниже код, при условии, 
что функция arithmetic_operation() написана правильно

add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))
должен выводить:

30
4.0
Примечание 2. Вызывать функцию arithmetic_operation() 
не нужно, требуется только реализовать ее.

Примечание 3. Модуль operator может быть полезен при решении этой задачи 
'''
# Решение
import operator

def arithmetic_operation(operation):
    if '+' == operation:
        return operator.add
    elif '-' == operation:
        return operator.sub
    elif '*' == operation:
        return operator.mul
    else:
        return operator.truediv

add = arithmetic_operation('+')
div = arithmetic_operation('/')

print(add(10, 20))
print(div(20, 5))