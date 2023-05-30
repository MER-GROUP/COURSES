'''
Это простое упражнение на написание декоратора.

Напишите декоратор с параметрами bucket, который будет делать так, 
что задекорированная функция, прежде чем возвращать результат, 
будет распечатывать в стандартный поток вывода все переданные 
bucket аргументы в следующем формате:  

  -  аргументы распечатаны в виде пары (кортежа размера два)
  -  первый элемент пары --  кортеж со значениями переданных 
  bucket аргументов без имени (значения в этом кортеже следуют 
  в том же порядке, в котором соответствующие аргументы были переданы bucket)
  -  второй элемент пары -- словарь с элементами вида имя: значение 
  для всех переданных bucket именованных аргументов.

from functools import wraps

def bucket('...'):
    '...'

Примеры ожидаемого поведения

@bucket(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', one = 1, two = 2, three = 3)
def identity(x):
  return x

print(identity(42))
>>> ((1, 2, 3, [1, 2, 3], 'one', 'two', 'three'), {'two': 2, 'one': 1, 'three': 3})
42


@bucket()
def identity(x):
  return x

print(identity(42))
>>> ((), {})
42 
'''
from functools import wraps

def bucket(*argsz, **kwargsz):
    def new_bucket(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print((argsz, kwargsz))
            return func(*args, **kwargs)
        return wrapper
    return new_bucket

if __name__ == '__main__':
    @bucket(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', one = 1, two = 2, three = 3)
    def identity(x):
        return x
    print(identity(42))

    @bucket()
    def identity(x):
        return x
    print(identity(42))