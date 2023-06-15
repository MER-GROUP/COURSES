'''
Декоратор returns
Реализуйте декоратор returns, который принимает один аргумент:

datatype — тип данных
Декоратор должен проверять, что возвращаемое значение декорируемой функции 
принадлежит типу datatype. Если возвращаемое значение принадлежит какому-либо 
другому типу, декоратор должен возбуждать исключение TypeError.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое 
значение декорируемой функции, а также должен уметь декорировать функции с 
произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый 
декоратор returns, но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640040/tests_3129779.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.8/Module_9.8.21

Sample Input 1:
@returns(int)
def add(a, b):
    return a + b
print(add(10, 5))
Sample Output 1:
15

Sample Input 2:
@returns(int)
def add(a, b):
    return a + b
try:
    print(add('199', '1'))
except TypeError as e:
    print(type(e))
Sample Output 2:
<class 'TypeError'>

Sample Input 3:
@returns(list)
def beegeek():
    'beegeek docs'
    return 'beegeek'
print(beegeek.__name__)
print(beegeek.__doc__)
try:
    print(beegeek())
except TypeError as e:
    print(type(e))
Sample Output 3:
beegeek
beegeek docs
<class 'TypeError'>

Sample Input 4:
@returns(list)
def append_this(li, elem):
    'append_this docs'
    return li + [elem]
print(append_this.__name__)
print(append_this.__doc__)
print(append_this([1, 2, 3], elem=4))
Sample Output 4:
append_this
append_this docs
[1, 2, 3, 4]
'''
from functools import wraps

def returns(datatype: callable):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            _res = func(*args, **kwargs)
            _check = isinstance(_res, datatype)
            if _check:
                return _res
            else:
                raise TypeError
        return wrapper
    return decorator

if __name__ == '__main__':
    @returns(int)
    def add(a, b):
        return a + b
    print(add(10, 5))

    @returns(int)
    def add(a, b):
        return a + b
    try:
        print(add('199', '1'))
    except TypeError as e:
        print(type(e))

    @returns(list)
    def beegeek():
        '''beegeek docs'''
        return 'beegeek'
    print(beegeek.__name__)
    print(beegeek.__doc__)
    try:
        print(beegeek())
    except TypeError as e:
        print(type(e))

    @returns(list)
    def append_this(li, elem):
        '''append_this docs'''
        return li + [elem]
    print(append_this.__name__)
    print(append_this.__doc__)
    print(append_this([1, 2, 3], elem=4))