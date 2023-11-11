print('------------------')

def greet(name):
    '''Функция приветствия пользователя.'''
    return f'Hello {name}!'

print(greet.__name__)
print(greet.__doc__)

print('------------------')

def bold(func):
    def wrapper(*args, **kwargs):
        return '<b>' + func(*args, **kwargs) + '</b>'
    return wrapper

@bold
def greet(name):
    '''Функция приветствия пользователя.'''
    return f'Hello {name}!'

print(greet.__name__)
print(greet.__doc__)

print('------------------')

def bold(func):
    def wrapper(*args, **kwargs):
        return '<b>' + func(*args, **kwargs) + '</b>'
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

@bold
def greet(name):
    '''Функция приветствия пользователя.'''
    return f'Hello {name}!'

print(greet.__name__)
print(greet.__doc__)

print('------------------')

import functools

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return '<b>' + func(*args, **kwargs) + '</b>'
    return wrapper

@bold
def greet(name):
    '''Функция приветствие пользователя.'''
    return f'Hello {name}!'

print(greet.__name__)
print(greet.__doc__)

print('------------------')

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Что-то выполняется до вызова декорируемой функции
        value = func(*args, **kwargs)
        # декорируется возвращаемое значение функции
        # или что-то выполняется после вызова декорируемой функции
        return value
    return wrapper

print('------------------')

import functools, time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        val = func(*args, **kwargs)
        end = time.perf_counter()
        work_time = end - start
        print(f'Время выполнения {func.__name__}: {round(work_time, 4)} сек.')
        return val
    return wrapper

@timer
def test(n):
    return sum([(i/99)**2 for i in range(n)])

@timer
def sleep(n):
    time.sleep(n)

res1 = test(10000)
res2 = sleep(4)

print(f'Результат функции test = {res1}')
print(f'Результат функции sleep = {res2}')

print('------------------')

import functools

def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.num += 1
        print(f'Вызов {func.__name__}: {wrapper.num}')
        val = func(*args, **kwargs)
        return val
    wrapper.num = 0
    return wrapper

@counter
def greet(name):
    return f'Hello {name}!'

print(greet('Timur'))
print(greet('Ruslan'))
print(greet('Arthur'))
print(greet('Gvido'))

print('------------------')

import functools
import time

def slow_down(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper

@slow_down
def countdown(number):
    if number < 1:
        print('Конец!')
    else:
        print(number)
        countdown(number - 1)
        
countdown(5)

print('------------------')

import sys, time
def teleprint(*args, delay=0.05, str_join=' '):
    text = str_join.join(str(x) for x in args)
    n = len(text)
    for i, char in enumerate(text, 1):
        if i == n:
            char = f'{char}\n'
        print(char, end='')
        time.sleep(delay)
        
teleprint('Привет Python!', 'Меня зовут Тимур', 'Beegeek = <3', str_join='*')
teleprint('Привет Python!', 'Меня зовут Тимур', 'Beegeek = <3', str_join='*')

print('------------------')

import functools

def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.num += 1
        print(f'Вызов {func.__name__}: {wrapper.num}')
        val = func(*args, **kwargs)
        return val
    wrapper.num = 0
    return wrapper

@counter
def greet1():
    return f'Hello Arthur!'

print(greet1())
print(greet1.num)

print('------------------')