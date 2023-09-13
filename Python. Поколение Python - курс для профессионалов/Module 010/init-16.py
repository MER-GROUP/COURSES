print('------------------')

from itertools import product

numbers = [1, 2]
letters = ['x', 'y', 'z']
flags = [False, True]

print(list(product(numbers, letters)))
print(list(product(letters, numbers)))
print(list(product(letters, numbers, flags)))

print('------------------')

from itertools import product

letters = 'abc'

print(list(product(letters, repeat=1)))
print(list(product(letters, repeat=2)))

print('------------------')

from itertools import product

numbers = [1, 2]
letters = ['x', 'y']

print(list(product(numbers, letters, repeat=1)))
print(list(product(numbers, letters, repeat=2)))
print(list(product(numbers, letters, numbers, letters, repeat=1)))

print('------------------')

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)

print('------------------')

from itertools import product

for time in product(range(24), range(60), range(60)):
    print(*time, sep=' : ')

print('------------------')

from itertools import product

ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз')
suits = ('треф', 'бубен', 'червей', 'пики')

cards = list(product(ranks, suits))

print(cards)

print('------------------')