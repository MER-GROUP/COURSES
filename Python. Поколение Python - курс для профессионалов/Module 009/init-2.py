print('------------------')

print(min([1, 2, 5, 7, 34, 6]))
print(min('a', 'b', 'ab'))
print(min([-3, 4, -90, 3, 45], key=abs))
print(min([], default='Empty'))

print('------------------')

print(max([1, 2, 5, 7, 34, 6]))
print(max('a', 'b', 'ab'))
print(max([-3, 4, -90, 3, 45], key=abs))
print(max([], default='Empty'))

print('------------------')

print(len([1, 2, 3, 4, 5, 6]))
print(len('abcdefg'))
print(len(range(10)))

print('------------------')

print(sum([1, 2, 3, 4, 5, 6]))
print(sum([], 99))

print('------------------')

for i in reversed([1, 2, 3, 4, 5]):
    print(i, end=' ')
print()
print(reversed([1, 2, 3]))
print(*reversed([1, 2, 3]))
print(type(reversed([1, 2, 3])))

print('------------------')

print(sorted([23, 4, 56, 6, 39]))
print(sorted([23, 4, 56, 6, 39], reverse=True))
print(sorted(['beegeek', 'step', 'python'], key=len))

print('------------------')

print(all([1, 2, 3]))   
print(all([1, 2, 3, 0, 5]))
print(all([True, 0, 1]))
print(all(('', 'red', 'green')))

print('------------------')

print(any([0, 0, 0]))
print(any([0, 1, 0]))
print(any([False, 0, 1]))
print(any(['', [], 'green']))

print('------------------')

colors = ['red', 'green', 'blue']

for pair in enumerate(colors, 1):
    print(pair)
print(enumerate(colors))
print(*enumerate(colors))
print(type(enumerate(colors)))

print('------------------')

print(*range(10))
print(*range(1, 10))
print(*range(2, 10, 2))

print('------------------')

my_range = range(1, 11)

print(my_range[0])
print(*my_range)
print(type(my_range))
print(my_range[1:4])
print(my_range.count(7))
print(my_range.index(10))
print(my_range == range(1, 10))

print('------------------')

numbers = [1, 2, 3]
words = ['one', 'two', 'three']
romans = ['I', 'II', 'III']

for number in zip(numbers, words, romans):
    print(number)
print(zip(numbers, words, romans))
print(*zip(numbers, words, romans))
print(type(zip(numbers, words, romans)))

print('------------------')

print(isinstance(3, int))
print(isinstance(3.5, (float, int, str)))
print(isinstance('Beegeek', str))
print(isinstance([1, 2, 3], list))
print(isinstance(True, bool))

print('------------------')

print(*[1, 2, 3, 4, 5], sep=', ', end='!')
print()

print('------------------')

print(type(3))
print(type(3.5))
print(type('Beegeek'))
print(type([1, 2, 3]))
print(type(True))

print('------------------')

print(list(range(50)).__sizeof__()) # 440
print(list(range(500)).__sizeof__()) # 4040
print(range(50).__sizeof__()) # 48
print(range(500).__sizeof__()) # 48
print(range(5000).__sizeof__()) # 48
print(range(50000).__sizeof__()) # 48

print('------------------')