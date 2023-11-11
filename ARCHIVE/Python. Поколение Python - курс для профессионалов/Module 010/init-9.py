print('------------------')

numbers = [1, 2, -9, 8, 3, -4, -2, -1, 0, 2, 91, 69]

odd_numbers = filter(lambda num: num % 2, numbers)
abs_odd_numbers = map(abs, odd_numbers)

print(*abs_odd_numbers)

print('------------------')

def integers(n):
    for i in range(1, n + 1):
        yield i

def evens(iterable):
    for i in iterable:
        if not i % 2:
            yield i

def squared(iterable):
    for i in iterable:
        yield i * i

def negated(iterable):
    for i in iterable:
        yield -i

chain = negated(squared(evens(integers(10))))

print(*chain)

print('------------------')

n = 10

integers = (i for i in range(1, n + 1))
evens = (i for i in integers if not i % 2)
squared = (i * i for i in evens)
negated = (-i for i in squared)

print(*negated)

print('------------------')

import typing

_gen = (i for i in range(5))  # генератор
_iter = iter(range(5))  # итератор

print(_gen)
print(_iter)

print(issubclass(_gen.__class__, typing.Iterator))
print(issubclass(_iter.__class__, typing.Generator))

print('------------------')