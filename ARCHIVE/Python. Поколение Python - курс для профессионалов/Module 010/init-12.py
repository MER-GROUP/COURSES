print('------------------')

from itertools import dropwhile

numbers = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
words = ['is', 'an', 'of', 'python', 'C#', 'beegeek', 'is']

new_numbers = list(dropwhile(lambda num: num <= 5, numbers))
print(new_numbers)

for word in dropwhile(lambda s: len(s) == 2, words):
    print(word)

print('------------------')

from itertools import dropwhile

def should_drop(x):
    print('Testing:', x)
    return x < 1

for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)

print('------------------')

def dropwhile(predicate, iterable):
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x

print('------------------')

from itertools import takewhile

numbers = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
words = ['is', 'an', 'of', 'python', 'C#', 'beegeek', 'is']

new_numbers = list(takewhile(lambda num: num <= 5, numbers))
print(new_numbers)

for word in takewhile(lambda s: len(s) == 2, words):
    print(word)

print('------------------')

from itertools import takewhile

def should_take(x):
    print('Testing:', x)
    return x < 2

for i in takewhile(should_take, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)

print('------------------')

from itertools import filterfalse

numbers = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
words = ['is', 'an', 'of', 'python', 'C#', 'beegeek', 'is']

new_numbers = list(filterfalse(lambda num: num <= 5, numbers))
print(new_numbers)

for word in filterfalse(lambda s: len(s) == 2, words):
    print(word)

print('------------------')

from itertools import filterfalse

def check_item(x):
    print('Testing:', x)
    return x < 1

for i in filterfalse(check_item, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)

print('------------------')

def filterfalse(predicate, iterable):
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x

print('------------------')

from itertools import compress

data = 'ABCDEF'
selectors = [True, False, True, False, True, False]

result = compress(data, selectors)
print(list(result))

print('------------------')

from itertools import compress

data = 'ABCDEF'
selectors = [True, False, True]

result = compress(data, selectors)
print(list(result))

print('------------------')

from itertools import islice

print(*islice(range(10), None))
print(*islice(range(100), 5))
print(*islice(range(100), 5, 10))
print(*islice(range(100), 0, 100, 10))

print('------------------')

def check_item(x):
    print('Testing:', x)
    return x < 1

for i in filter(check_item, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)

print('------------------')