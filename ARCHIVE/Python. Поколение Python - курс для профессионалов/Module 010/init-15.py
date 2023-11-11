print('------------------')

from itertools import permutations

numbers = [1, 2, 3, 4]
letters = 'cba'

all_num_permutations = permutations(numbers)
all_let_permutations = permutations(letters)

print(list(all_num_permutations))
print(list(all_let_permutations))

print('------------------')

from itertools import permutations

letters = ['a', 'b', 'c']

permutations1 = permutations(letters, r=1)
permutations2 = permutations(letters, r=2)
permutations3 = permutations(letters, r=3)

print(list(permutations1))
print(list(permutations2))
print(list(permutations3))

print('------------------')

from itertools import permutations

numbers = [1, 2, 2]

num_permutations = permutations(numbers)

print(list(num_permutations))

print('------------------')

from itertools import combinations

numbers = [1, 2, 3, 4]

print(list(combinations(numbers, r=1)))
print(list(combinations(numbers, r=2)))
print(list(combinations(numbers, r=3)))
print(list(combinations(numbers, r=4)))

print('------------------')

from itertools import combinations

letters = 'dbca'

print(list(combinations(letters, 1)))
print(list(combinations(letters, 2)))
print(list(combinations(letters, 3)))
print(list(combinations(letters, 4)))

print('------------------')

from itertools import combinations

letters = [1, 2, 2, 2]

print(list(combinations(letters, 2)))

print('------------------')

from itertools import combinations_with_replacement

numbers = [1, 2, 3, 4]

print(list(combinations_with_replacement(numbers, 1)))
print(list(combinations_with_replacement(numbers, 2)))
print(list(combinations_with_replacement(numbers, 3)))

print('------------------')

from itertools import combinations_with_replacement

letters = 'bca'

print(list(combinations_with_replacement(letters, 1)))
print(list(combinations_with_replacement(letters, 2)))

print('------------------')