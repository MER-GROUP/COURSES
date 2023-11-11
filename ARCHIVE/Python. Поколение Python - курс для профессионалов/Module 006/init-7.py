print('------------------')

from collections import OrderedDict

numbers = OrderedDict()

numbers['one'] = 1
numbers['two'] = 2
numbers['three'] = 3

print(numbers)

print('------------------')

from collections import OrderedDict

numbers1 = OrderedDict({'one': 1, 'two': 2, 'three': 3})
numbers2 = OrderedDict([('one', 1), ('two', 2), ('three', 3)])
numbers3 = OrderedDict(one=1, two=2, three=3)

print('------------------')

from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)
print(numbers)

numbers['four'] = 4
print(numbers)

print('------------------')

from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)
print(numbers)

del numbers['one']
print(numbers)

numbers['one'] = 1
print(numbers)

# print({1:1, 2:2, 3:3})

print('------------------')

from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)
print(numbers)

numbers['one'] = 1.0
print(numbers)

numbers.update(two=2.0)
print(numbers)

print('------------------')

from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)

# обращение по ключу
print(numbers['one'])
print(numbers['three'])
print()

# перебор ключей напрямую
for key in numbers:
    print(key, '->', numbers[key])
print()

# перебор пар (ключ, значение) через метод
for key, value in numbers.items():
    print(key, '->', value)
print()

# перебор ключей через метод
for key in numbers.keys():
    print(key, '->', numbers[key])
print()

# перебор значение через метод
for value in numbers.values():
    print(value)

print('------------------')

from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)

# перебор ключей напрямую
for key in reversed(numbers):
    print(key, '->', numbers[key])
print()

# перебор пар (ключ, значение) через метод
for key, value in reversed(numbers.items()):
    print(key, '->', value)
print()

# перебор ключей через метод
for key in reversed(numbers.keys()):
    print(key, '->', numbers[key])
print()

# перебор значений через метод
for value in reversed(numbers.values()):
    print(value)

print('------------------')

from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)
print(numbers)

numbers.move_to_end('one') # last=True
print(numbers)

numbers.move_to_end('three', last=False) # last=False
print(numbers)

print('------------------')

from collections import OrderedDict

letters = OrderedDict(b=2, d=4, a=1, c=3)

for key in sorted(letters):
    letters.move_to_end(key)

print(letters)

print('------------------')

from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)

print(numbers.popitem())
print(numbers)

print(numbers.popitem())
print(numbers)

print('------------------')

from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)

print(numbers.popitem(last=False))
print(numbers)

print(numbers.popitem(last=False))
print(numbers)

print('------------------')

letters1 = dict(a=1, b=2, c=3, d=4)
letters2 = {'b': 2, 'a': 1, 'c': 3, 'd': 4}
letters3 = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

print(letters1 == letters2)
print(letters1 == letters3)

print('------------------')

from collections import OrderedDict

letters1 = OrderedDict(a=1, b=2, c=3, d=4)
letters2 = OrderedDict({'b': 2, 'a': 1, 'c': 3, 'd': 4})
letters3 = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

print(letters1 == letters2)
print(letters1 == letters3)

print('------------------')

from collections import OrderedDict

letters1 = OrderedDict(a=1, b=2, c=3, d=4)
letters2 = {'b': 2, 'a': 1, 'c': 3, 'd': 4}

print(letters1 == letters2)

print('------------------')

from collections import OrderedDict

keys = ['one', 'two', 'three']
numbers = OrderedDict.fromkeys(keys, 0)
print(numbers)

print('------------------')

from collections import OrderedDict

physicists = OrderedDict(newton='1642-1726', einstein='1879-1955')
biologists = OrderedDict(darwin='1809-1882', mendel='1822-1884')

scientists = physicists | biologists
print(scientists)

print('------------------')

from collections import OrderedDict

physicists = OrderedDict(newton='1642-1726', einstein='1879-1955')
physicists1 = OrderedDict(newton='1642-1726/1727', hawking='1942-2018')

physicists |= physicists1

print(physicists)

print('------------------')

from collections import OrderedDict

letters = OrderedDict(b=2, d=4, a=1, c=3)
print(letters)
print(letters.__dict__)

letters.__dict__['advanced'] = '144'
print(letters)
print(letters.__dict__)

print('------------------')

# letters = dict(b=2, d=4, a=1, c=3)
# # у обычных словарей нет атрибута __dict__
# print(letters.__dict__)    

print('------------------')

from collections import OrderedDict

letters = OrderedDict(b=2, d=4, a=1, c=3)

letters.sorted_keys = lambda: sorted(letters.keys())

print(letters)
print(letters.sorted_keys())

letters['e'] = 5
print(letters)
print(letters.sorted_keys())

for key in letters.sorted_keys():
    print(key, '->', letters[key])

print('------------------')

num = 10

func = lambda: num**2
print(func())

print('------------------')