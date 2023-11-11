print('------------------')

list_iterator = iter([1, 2, 3])       # итератор на основе списка
str_iterator = iter('beegeek')        # итератор на основе строки

print('------------------')

list_iterator = iter([1, 2, 3])
str_iterator = iter('beegeek')

print(next(list_iterator))
print(next(list_iterator))

print(next(str_iterator))
print(next(str_iterator))
print(next(str_iterator))

print('------------------')

# list_iterator = iter([1, 2, 3])

# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))

# print(next(list_iterator))

print('------------------')

list_iterator = iter([1, 2, 3])
new_iterator = iter(list_iterator)

print(list_iterator is new_iterator)

print('------------------')

list_iterator = iter([1, 2, 3])

print(list(list_iterator))         # получаем все элементы итератора
print(list(list_iterator))

print('------------------')

list_iterator = iter([1, 2, 3])

print(2 in list_iterator)
print(2 in list_iterator)
print(2 in list_iterator)

print('------------------')

numbers = [1, 2, 3]

print(enumerate(numbers))
print(zip(numbers, numbers))
print(reversed(numbers))

print('------------------')

numbers = [1, 2, 3]

squares = (n**2 for n in numbers)
print(squares)

print('------------------')

for i in range(3):
    print(i)

print(list(range(5, 10)))
print(tuple(range(5, 50, 5)))

print('------------------')

range_iterator = iter(range(3))

print(range_iterator)

print('------------------')

# range_obj = range(3)

# print(next(range_obj))

print('------------------')

range_obj = range(3)

print(list(range_obj))
print(list(range_obj))

print('------------------')

range_obj = range(5, 50, 5)

print(*range_obj)
print(len(range_obj))
print(range_obj[3])
print(range_obj[-1])
print(range_obj[4:8])

print('------------------')

range_obj = range(5, 50, 5)

print(15 in range_obj)
print(15 in range_obj)
print(15 in range_obj)

print('------------------')

range1 = range(10)
range2 = range(3, 20)
range3 = range(5, 50, 10)

print(range1.start, range1.step, range1.stop)
print(range2.start, range2.step, range2.stop)
print(range3.start, range3.step, range3.stop)

print('------------------')

range1 = range(10)
range2 = range(0, 10, 1)
range3 = range(5, 50, 10)

print(range1 == range2)
print(range1 == range3)

print('------------------')

print(range(0) == range(2, 1, 3))
print(range(0, 3, 2) == range(0, 4, 2))

print('------------------')

iterable1 = [1, 2, 3]
iterable2 = ['a', 'b', 'c']
iterable3 = ['A', 'B', 'C']

print(*zip(iterable1))                          # (1,) (2,) (3,)
print(*zip(iterable1, iterable2))               # (1, 'a') (2, 'b') (3, 'c')
print(*zip(iterable1, iterable2, iterable3))    # (1, 'a', 'A') (2, 'b', 'B') (3, 'c', 'C')

print('------------------')