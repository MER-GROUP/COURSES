print('------------------')

from sys import getsizeof

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
letters = 'beegeek'

squares = map(lambda num: num ** 2, numbers)
capitals = map(str.upper, letters)

print(f'Тип итератора squares: {type(squares)}, размер: {getsizeof(squares)}')
print(f'Тип итератора capitals: {type(capitals)}, размер: {getsizeof(capitals)}')

print(*squares, sep=' ')
print(*capitals, sep=' ')

print('------------------')

from sys import getsizeof

numbers = [45, -90, -21, 4, 89, 43, 1234, 112, 999, 777, -765, -666]
objects = ('a', None, 45, True, 69.69, False, -1, 0, 'empty', '')

positive_numbers = filter(lambda num: num > 0, numbers)
not_nulls = filter(None, objects)

print(f'Тип итератора positive_numbers: {type(positive_numbers)}, размер: {getsizeof(positive_numbers)}')
print(f'Тип итератора not_nulls: {type(not_nulls)}, размер: {getsizeof(not_nulls)}')

print(*positive_numbers, sep=' ')
print(*not_nulls, sep=' ')

print('------------------')

from sys import getsizeof

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
letters = 'beegeek'

numbered_seasons = enumerate(seasons)
numbered_letters = enumerate(letters, start=1)

print(f'Тип итератора numbered_seasons: {type(numbered_seasons)}, размер: {getsizeof(numbered_seasons)}')
print(f'Тип итератора numbered_letters: {type(numbered_letters)}, размер: {getsizeof(numbered_letters)}')

print(*numbered_seasons, sep=' ')
print(*numbered_letters, sep=' ')

print('------------------')

from sys import getsizeof

languages = ['Python', 'C#', 'C', 'Delphi'] 
years = [1991, 2000, 1972, 1986]
authors = ('Guido van Rossum', 'Anders Hejlsberg', 'Dennis MacAlistair Ritchie', 'Anders Hejlsberg')

zip_iterator1 = zip(languages, years)
zip_iterator2 = zip(languages, years, authors)
zip_iterator3 = zip(languages)
zip_iterator4 = zip([])

print(f'Тип итератора zip_iterator1: {type(zip_iterator1)}, размер: {getsizeof(zip_iterator1)}')
print(f'Тип итератора zip_iterator2: {type(zip_iterator2)}, размер: {getsizeof(zip_iterator2)}')

print(*zip_iterator1, sep=' ')
print(*zip_iterator2, sep=' ')
print(*zip_iterator3, sep=' ')
print(*zip_iterator4, sep=' ')

print('------------------')

from sys import getsizeof

years = [1991, 2000, 1972, 1986]
letters = 'beegeek'

backward_years = reversed(years)
backward_letters = reversed(letters)

print(f'Тип итератора backward_years: {type(backward_years)}, размер: {getsizeof(backward_years)}')
print(f'Тип итератора backward_letters: {type(backward_letters)}, размер: {getsizeof(backward_letters)}')

print(*backward_years, sep=' ')
print(*backward_letters, sep=' ')

print('------------------')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = map(lambda num: num ** 2, numbers)
cubes = map(lambda num: num ** 3, numbers)

print(max(squares))
print(min(cubes))

print('------------------')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = map(lambda num: num ** 2, numbers)
cubes = map(lambda num: num ** 3, numbers)

print(max(squares))
print(min(cubes))

print(list(squares))
print(list(cubes))

print('------------------')

numbers = {1, 2, 3, 4, 5}

for item in numbers:
    print(item, end=' ')  # 1 2 3 4 5

print('------------------')