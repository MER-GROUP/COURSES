print('------------------')

import functools

def stars(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('*' * 30)
        return func(*args, **kwargs)
    return wrapper

def lines(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('-' * 10)
        return func(*args, **kwargs)
    return wrapper

def equals(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('=' * 40)
        return func(*args, **kwargs)
    return wrapper

@stars
def add(a, b):
    return a + b

@lines
def mult(a, b):
    return a * b

@equals
def diff(a, b):
    return a - b

print(add(3, 9))
print(mult(10, 20))
print(diff(100, 1))

print('------------------')

def print_symbols(symbol, length):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(symbol * length)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@print_symbols('*', 30)
def add(a, b):
    return a + b

@print_symbols('-', 10)
def mult(a, b):
    return a * b

@print_symbols('=', 40)
def diff(a, b):
    return a - b

print(add(3, 9))
print(mult(10, 20))
print(diff(100, 1))

print('------------------')

import functools
import time

def delayed(delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'Спим {delay} сек.')
            time.sleep(delay)
            value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator

@delayed(1)
def countdown(number):
    if number < 1:
        print('Конец!')
    else:
        print(number)
        countdown(number - 1)
        
countdown(5)

print('------------------')

import functools, time

def timer(iters=1):
    def decorator(func):   
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.perf_counter()
                value = func(*args, **kwargs)
                end = time.perf_counter()
                total += end - start
            print(f'Среднее время выполнения {func.__name__}: {round(total/iters, 4)} сек.')
            return value
        return wrapper
    return decorator

@timer(iters=1000)
def test(n):
    return sum([(i/99)**2 for i in range(n)])

@timer(iters=3)
def sleep(n):
    time.sleep(n)

res1 = test(10000)
res2 = sleep(4)

print(f'Результат функции test = {res1}')
print(f'Результат функции sleep = {res2}')

print('------------------')

import functools

def repeater(repeat=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, repeat + 1):
                print(f'{i}-й запуск функции.')
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator

@repeater(repeat=5)
def beegeek():
    print('beegeek')

beegeek()

print('------------------')

# @repeater
# def beegeek():
#     print('beegeek')

# beegeek()

print('------------------')

# используется значение по умолчанию repeat=1
@repeater()                       
def beegeek():
    print('beegeek')

beegeek()

print('------------------')

import functools
import time

def repeater(repeat=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, repeat + 1):
                print(f'{i}-й запуск функции.')
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator

def delayed(delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'Спим {delay} сек.')
            time.sleep(delay)
            value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator

@repeater(repeat=5)
@delayed(delay=1)
def monitor(url):
    print(f'Проверка {url} на доступность.')
    
monitor('https://stepik.org/')

print('------------------')

@delayed(delay=1)
@repeater(repeat=5)
def monitor(url):
    print(f'Проверка {url} на доступность.')
    
monitor('https://stepik.org/')

print('------------------')

import functools

def repeater(func=None, repeat=1):
    if not func:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for i in range(1, repeat + 1):
                    print(f'{i}-ый запуск функции.')
                    value = func(*args, **kwargs)
                return value
            return wrapper
        return decorator
    else:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, repeat + 1):
                print(f'{i}-ый запуск функции.')
                value = func(*args, **kwargs)
            return value
        return wrapper

@repeater(repeat=1)
def beegeek():
    print('beegeek')

beegeek()
print()

@repeater
def beegeek():
    print('beegeek')

beegeek()

print('------------------')