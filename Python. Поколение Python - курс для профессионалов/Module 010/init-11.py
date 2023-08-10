print('------------------')

from itertools import count

count1 = count()

print(next(count1))
print(next(count1), next(count1), next(count1))

count2 = count(69, 10)

print(next(count2))
print(next(count2))
print(next(count2), next(count2), next(count2))

for i in zip(count(10), ['a', 'b', 'c']):
    print(i)

print('------------------')

from itertools import count
from fractions import Fraction

for index, number in enumerate(count(1.0, 0.5)):
    if index < 6:
        print(number)
    else:
        break

frac_iter = count(1, Fraction(1, 2))
print(next(frac_iter), next(frac_iter), next(frac_iter), next(frac_iter), next(frac_iter))

print('------------------')

def count(start=0, step=1):
    n = start
    while True:
        yield n
        n += step

print('------------------')

from itertools import cycle

for index, char in enumerate(cycle('abcd')):
    if index < 7:
        print(char)
    else:
        break

cycle_iter = cycle([0, 1])
print(next(cycle_iter), next(cycle_iter), next(cycle_iter), next(cycle_iter), next(cycle_iter))

for i in zip(range(7), cycle(['a', 'b', 'c'])):
    print(i)

print('------------------')

def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element

print('------------------')

from itertools import repeat

for i in repeat('bee-and-geek', 5):
    print(i)

repeat_iter = repeat([1, 2, 3])

print(next(repeat_iter))
print(next(repeat_iter))
print(next(repeat_iter))

print('------------------')

from itertools import count, repeat

for i, s in zip(count(), repeat('bee-and-geek', 5)):
    print(i, s)

print('------------------')

from itertools import repeat

for a, b, c in map(lambda x, у: (x, у, x * у), repeat(2), range(6)):
    print(f'{a} * {b} = {c}')

print('------------------')

from itertools import starmap

persons = [('Timur', 'Guev'), ('Arthur', 'Kharisov')]
pairs = [(1, 3), (2, 5), (6, 4)]
points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]

full_names = list(starmap(lambda name, surname: f'{name} {surname}', persons))

print(full_names)
print(*starmap(lambda a, b: a + b, pairs))
print(*starmap(lambda x, y, z: x * y * z, points))

print('------------------')

def starmap(function, iterable):
    for args in iterable:
        yield function(*args)

print('------------------')

from itertools import accumulate
import operator

data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]

print(list(accumulate(data)))
print(list(accumulate(data, operator.mul)))
print(list(accumulate(data, max)))
print(list(accumulate(data, min)))

print('------------------')

from itertools import accumulate

print(list(accumulate([1, 2, 3, 4, 5], initial=100)))

print('------------------')

# import itertools as it
# import time

# symbols = ['.', '-', "'", '"', "'", '-', '.', '_']

# for c in it.cycle(symbols):
#     print(c, end='')
#     time.sleep(0.05)

print('------------------')

import time

symbols = ['.', '-', "'", '"', "'", '-', '.', '_']

while True:
    symbols = '\r' + symbols.pop() + ''.join(symbols)
    print(symbols, end='')
    symbols = list(symbols)[1:]
    time.sleep(0.1)

print('------------------')