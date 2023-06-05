'''
Это упражнение на написание декоратора.

Определите новую версию декоратора apply, которая может 
принимать аргументы, и, соответственно, при декорировании 
некоторой функции apply установит переменную с именем 
задекорированной функции в значение этой функции на 
переданных apply аргументах.

def apply('...'):
    '...'

Примеры ожидаемого поведния

@apply(2, 3)
def multiply(x, y):
    return x * y
    
print(multiply, type(multiply))
 
>>> 6, <class 'int'>
'''
from functools import wraps, partial

def apply(*argsz, **kwargsz):
    def new_apply(func):
        if argsz or kwargsz:
            return func(*argsz, **kwargsz)  
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return new_apply

if __name__ == '__main__':
    @apply(2, 3)
    def multiply(x, y):
        return x * y
        
    print(multiply, type(multiply))