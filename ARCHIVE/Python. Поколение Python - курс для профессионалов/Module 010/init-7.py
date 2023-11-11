print('------------------')

def get_data():
    for num in range(5):
        yield num
    for char in 'ABC':
        yield char

for i in get_data():
    print(i)

print('------------------')

def get_data():
    yield from range(5)
    yield from 'ABC'

print('------------------')

def chain(*iterables):
    for it in iterables:
        for value in it:
            yield value

for i in chain('AB', [1, 2], (4, 5), {'name': 'Timur', 'age': 29}):
    print(i, end=' ')

print()
print('------------------')

def chain(*iterables):
    for it in iterables:
        yield from it

print('------------------')

def generator2():
    yield 'Red'
    yield 'Blue'

def generator1():
    yield 'Green'
    # запрашиваем значение из субгенератора
    yield from generator2()            
    yield 'Yellow'
    yield 'Black'

for color in generator1():
    print(color, end=' ')

print()

print('------------------')

def numbers(start):
    if not isinstance(start, int):
        raise TypeError('Аргументом должно быть целое число')
    yield start
    yield from numbers(start + 1)

for index, number in enumerate(numbers(3)):
    if index > 5:
        break
    print(number)

print('------------------')