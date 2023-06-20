print('------------------')

def fib(n):
    cache = {1: 1, 2: 1}
    def fib_rec(n):
        result = cache.get(n)
        if result is None:
            result = fib_rec(n - 2) + fib_rec(n - 1)
            cache[n] = result
        return result
    return fib_rec(n)

print('------------------')

import functools

def cached(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        result = cache.get(key)
        if result is None:
            result = func(*args, **kwargs)
            cache[key] = result
        return result
    return wrapper

print('------------------')

from functools import lru_cache

@lru_cache()
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print('------------------')

from functools import lru_cache

@lru_cache(typed=False)
def concat(text, num):
    return text + ' ' + str(num)

print(concat('beegeek', 4))
print(concat('beegeek', 5.0))
print(concat('beegeek', 4.0))

print('------------------')

from functools import lru_cache

@lru_cache(typed=True)
def concat(text, num):
    return text + ' ' + str(num)

print(concat('beegeek', 4))
print(concat('beegeek', 5.0))
print(concat('beegeek', 4.0))

print('------------------')

from functools import lru_cache

@lru_cache(typed=False)
def concat(text, num):
    return text + ' ' + str(num)

print(concat('beegeek', 1))
print(concat('beegeek', 1.0))
print(concat('beegeek', True))
print(concat('beegeek', 4.0))
print(concat('beegeek', 5))

print(concat.cache_info())

print('------------------')

from functools import lru_cache

@lru_cache(typed=False)
def concat(text, num):
    return text + ' ' + str(num)

print(concat('beegeek', 1))
print(concat('beegeek', 1.0))
print(concat('beegeek', True))
print(concat('beegeek', 4.0))
print(concat('beegeek', 5))

print(concat.cache_info())
concat.cache_clear()
print(concat.cache_info())

print('------------------')