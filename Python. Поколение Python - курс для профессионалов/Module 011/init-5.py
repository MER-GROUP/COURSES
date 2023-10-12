print('------------------')

import re

text = 'ул. Часовая, дом № 25, корпус 2, квартира 69'
result = re.findall('\d+', text)

print(result)

print('------------------')

import re

result = re.findall('#(\w+)#', '#foo#.#bar#.#baz#')

print(result)

print('------------------')

import re

result1 = re.findall('(\w+),(\w+)', 'foo,bar,baz,qux,quux,corge')
result2 = re.findall('(\w+),(\w+),(\w+)', 'foo,bar,baz,qux,quux,corge')

print(result1)
print(result2)

print('------------------')

import re

result = re.findall('(\w+),(\w+),(\w+)?', 'foo,bar,')

print(result)

print('------------------')

import re

result = re.findall('(\w+),(\w+),(\w+)', 'foo,bar,')

print(result)

print('------------------')

import re

text = 'ул. Часовая, дом № 25, корпус 2, квартира 69'
result = re.finditer('\d+', text)

print(type(result))
print(list(result))

print('------------------')

import re

result = re.finditer('#(\w+)#', '#foo#.#bar#.#baz#')

for match in result:
    print(match)
    print(match.group(), match.group(1))

print('------------------')