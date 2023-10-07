print('------------------')

from re import search

match1 = search('super', 'superstition')
match2 = search('super', 'insuperable')
match3 = search('super', 'without')

print(match1)
print(match2)
print(match3)

print('------------------')

from re import search

match1 = search('\d+', 'foo123bar')
match2 = search('[a-z]+', '123FOO456')
match3 = search('\d+', 'foo.bar')

print(match1)
print(match2)
print(match3)

print('------------------')

from re import match

match1 = match('super', 'superstition')
match2 = match('super', 'insuperable')

print(match1)
print(match2)

print('------------------')

from re import search, match

match1 = search('\d+', '123foobar')
match2 = search('\d+', 'foo123bar')
match3 = match('\d+', '123foobar')
match4 = match('\d+', 'foo123bar')

print(match1)
print(match2)
print(match3)
print(match4)

print('------------------')

from re import fullmatch

match1 = fullmatch('\d+', '123foo')
match2 = fullmatch('\d+', 'foo123')
match3 = fullmatch('\d+', 'foo123bar')
match4 = fullmatch('\d+', '123')

print(match1)
print(match2)
print(match3)
print(match4)

print('------------------')

from re import search

match = search('^\d+$', '123')
print(match)

print('------------------')

from re import fullmatch

phone_pattern = '\d{3}-\d{3}-\d{4}'

match1 = fullmatch(phone_pattern , '777-888-1234')
match2 = fullmatch(phone_pattern , '77-89-56')
match3 = fullmatch(phone_pattern , '5555-99-1234')
match4 = fullmatch(phone_pattern , '123-000-3333ab')

print(match1)
print(match2)
print(match3)
print(match4)

print('------------------')

from re import search, fullmatch

match = fullmatch('\d{3}-\d{3}-\d{4}', '777-888-1234')

if match:
    print('Строка соответствует формату.')
    print(match)
else:
    print('Строка не соответствует формату.')

print('------------------')

from re import search

match = search('(\w+),(\w+),(\w+)', 'foo,bar,baz')

print(match.group())                       # вся строка
print(match.group(0))                      # вся строка
print(match.group(1))                      # подгруппа
print(match.group(2))                      # подгруппа
print(match.group(3))                      # подгруппа
print(match.group(1, 2, 3))                # кортеж

print('------------------')

# from re import search

# match = search('(\w+),(\w+),(\w+)', 'foo,bar,baz')
# print(match.group(4))

print('------------------')

from re import search

match = search('(\w+),(\w+),(\w+)', 'foo,bar,baz')
print(match.group(1, 2, 3, 1, 2, 2, 3, 3, 3, 3))

print('------------------')

from re import search

match = search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,bar,baz')

print(match.group())
print(match.group('w1'))
print(match.group('w2'))
print(match.group('w3'))
print(match.group('w1', 'w2', 'w3', 'w2', 'w3'))

print('------------------')

from re import search

match = search('(\w+),(\w+),(\w+)?', 'foo,bar,')

print(match.group())
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(3))
print(match.group(1, 2, 3))

print('------------------')

from re import search

match = search('(\w+),(\w+),(\w+)?', 'foo,bar,')
print(match.groups())

print('------------------')

from re import search

match = search('(\w+),(\w+),(\w+)?', 'foo,bar,')

print(match.groups(-1))                     # позиционный аргумент
print(match.groups(''))
print(match.groups(default='----'))         # именованный аргумент
print(match.groups(default=False))

print('------------------')

from re import search

match = search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,bar,baz')
print(match.groupdict())

print('------------------')

from re import search

match = search('(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)?', 'foo,bar,')

print(match.groupdict())
print(match.groupdict(default=''))
print(match.groupdict(default='----'))

print('------------------')

from re import search

match = search('(\w+),(\w+),(\w+)?', 'foo,bar,buz')

print(match.groupdict())
print(match.groupdict(default=''))
print(match.groupdict(default='----'))

print('------------------')

from re import search

match = search('\d+', 'foo123bar456baz')

print(match)
print(match.start())
print(match.end())

print('------------------')

from re import search

text = 'foo123bar456baz'

match = search('\d+', text)

start = match.start()
end = match.end()

print(match)
print(text[start:end])
print(match.group())           # аналогично предыдущей строке

print('------------------')

from re import search

text = 'foo123bar456baz'

match = search('(\d+)\D+(?P<num>\d+)', text)

print(match)
print(match.group(), match.start(), match.end())
print(match.group(1), match.start(1), match.end(1))
print(match.group('num'), match.start('num'), match.end('num'))

print('------------------')

from re import search

match = search('foo(\d*)bar', 'foobar')

print(match)
print(match.group())
print(match.start(), match.end())
print(match.start(1), match.end(1))

print('------------------')

from re import search

match = search('(\w+),(\w+),(\w+)?', 'foo,bar,')

print(match.group(3))
print(match.start(3), match.end(3))

print('------------------')

from re import search

match = search('(\d+)\D+(?P<num>\d+)', 'foo123bar456baz')

print(match)
print(match.span())
print(match.span(1))
print(match.span('num'))

print('------------------')