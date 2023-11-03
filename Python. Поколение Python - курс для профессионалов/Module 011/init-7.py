print('------------------')

# по умолчанию разбиваем через пробельные символы
print('stepik beegeek       python'.split())             
print('aaa,bbbb,ccccc'.split(','))
print('hello---world---from---beegeek'.split('---'))

print('------------------')

import re

result = re.split(r'[,;.]', 'foo,bar.baz;qux;stepik,beegeek')

print(result)

print('------------------')

import re

result = re.split(r'\s*[,;.]\s*', 'foo,   bar. baz   ;    qux ;  stepik   ,   beegeek')

print(result)

print('------------------')

import re

result1 = re.split(r'\s*([,;.])\s*', 'foo,   bar. baz   ;    qux ;  stepik   ,   beegeek')
result2 = re.split(r'(\s*[,;.]\s*)', 'foo,   bar. baz   ;    qux ;  stepik   ,   beegeek')

print(result1)
print(result2)

print('------------------')

import re

string = 'foo,bar.baz;  qux;stepik,    beegeek'
regex = r'(\s*[,;.]\s*)'

result = re.split(regex, string)

for index, value in enumerate(result):
    if not re.fullmatch(regex, value):
        result[index] = f'[{value}]'

new_string = ''.join(result)

print(string)
print(new_string)

print('------------------')

import re

result = re.split(r'(?:\s*[,;.]\s*)', 'foo,   bar. baz   ;    qux ;  stepik   ,   beegeek')

print(result)

print('------------------')

import re

text = 'foo; bar;   baz; qux;   stepik;    beegeek'
regex = r';\s*'

result1 = re.split(regex, text)
result2 = re.split(regex, text, maxsplit=2)
result3 = re.split(regex, text, maxsplit=4)

print(result1)
print(result2)
print(result3)

print('------------------')

text = 'foo;bar;baz;beegeek;stepik;python'

print(text.split(sep=';', maxsplit=2))

print('------------------')

import re 

result = re.split(r'(/)', '/beegeek/stepik/python/')

print(result)

print('------------------')

result = '/beegeek/stepik/python/'.split('/')

print(result)

print('------------------')

result = ' beegeek stepik python '.split(' ')

print(result)

print('------------------')

result = ' beegeek stepik python '.split()

print(result)

print('------------------')

import re

result = re.split(r'\D+', '1 + 2 - 3 * 4')

print(result)

print('------------------')