print('------------------')

print(callable(int))
print(callable(list))
print(callable(100))
print(callable([1, 2, 3]))

print('------------------')

print(hasattr('stepik', 'isalpha'))
print(hasattr([1, 2, 3], 'sort'))
print(hasattr(13, 'to_str'))

print('------------------')

print(hash(899))
print(hash(69.0))
print(hash('timyrik'))
print(hash((1, 2, 3)))
print(hash(False))
print(hash(True))

print('------------------')

for i in range(-5, 6):
    print(hash(i))

print('------------------')

tpl = (1, 2, True, 'python')
print(hash(tpl))

print('------------------')

# tpl = (1, 2, [True, 'python'])
# print(hash(tpl))

print('------------------')

help(print)
help('sorted')

print('------------------')

from datetime import date

print(repr('stepik'))
print(repr([1, 2, 3, 4]))
print(repr(date(2022, 1, 16)))

print('------------------')

from datetime import date

td = date.today()
print(f"{td!r}")

print('------------------')