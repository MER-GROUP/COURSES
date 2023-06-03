'''
Это упражнение на написание декоратора

Завершите определение декоратора decorator из предыдущего видео.

По возможности, не переписывайте уже сделанное там, а воспроизведите 
процесс построения для себя ещё раз.

Когда напишете правильное определение, убедитесь, что вы понимаете, 
как декоратор decorator устроен, как это всё работает.
'''
from functools import wraps

def decorator(decor):
    def new_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return decor(func, *args, **kwargs)
        return wrapper
    return new_decorator

@decorator
def introduce(f, *args, **kwargs):
    print(f.__name__)
    return f(*args, **kwargs)

@introduce
def identity(x):
    return x

if __name__ == '__main__':
    print(identity(31415))