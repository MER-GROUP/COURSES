'''
Это упражнение на написание декоратора.

Перепишите декоратор bucket из первой задачи так, чтобы он был определён 
при помощи partial, по аналогии с определением introduce из предыдущего видео.

Как уже говорилось в видео, при таком способе определения мы допускаем 
наличие у декоратора только именованных параметров, поэтому теперь 
вместо пары из кортежа с аргументами без имени и словаря с именованными 
аргументами нужно просто печатать словарь с именованными аргументами.

from functools import wraps, partial

def bucket('...'):
    '...'

Примеры ожидаемого поведения

@bucket(one = 1, two = 2, three = 3)
def identity(x):
  return x

print(identity(42))
>>> {'two': 2, 'one': 1, 'three': 3}
42

@bucket
def identity(x):
  return x

print(identity(42))
>>> {}
42
'''
from functools import wraps, partial

# # старая реализация bucket
# def bucket(*argsz, **kwargsz):
#     def new_bucket(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print((argsz, kwargsz))
#             return func(*args, **kwargs)
#         return wrapper
#     return new_bucket

def bucket(func=None, **keywords):
    if func is None:
        return partial(bucket, **keywords)
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(keywords)
        return func(*args, **kwargs)
    return wrapper

if __name__ == '__main__':
    @bucket(one = 1, two = 2, three = 3)
    def identity(x):
        return x
    print(identity(42))

    @bucket
    def identity(x):
        return x
    print(identity(42))