'''
Это простое упражнение на использование упаковок.

Определите функцию print_given, которая для каждого переданного 
аргумента будет распечатывать на отдельной строке через пробел 
имя аргумента (если таковое имеется), значение аргумента, тип аргумента.

Аргументы без имени должны быть распечатаны раньше именованных. 
Порядок печати аргументов без имени важен: он должен совпадать 
с порядком, в котором аргументы передаются. Порядок печати аргументов с именем неважен.


Примеры ожидаемого поведения:

print_given(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two = 2, one = 1, three = 3)
>>> 1 <class 'int'> 
2 <class 'int'>
3 <class 'int'>
[1, 2, 3] <class 'list'>
one <class 'str'>
two <class 'str'>
three <class 'str'>
one 1 <class 'int'>
two 2 <class 'int'>
three 3 <class 'int'>

print_given()
'''
def print_given(*args, **kwargs):
    [print(f'{el} {type(el)}') for el in args]
    [print(f'{k} {v} {type(v)}') for k, v in kwargs.items()]

if __name__ == '__main__':
    print_given(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two = 2, one = 1, three = 3)
    print('----------')
    print_given()