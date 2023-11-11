print('------------------')

import re

text = 'Java самый популярный язык программирования в 2022 году.'

res = re.sub(r'Java', r'Python', text)

print(res)

print('------------------')

import re

text = 'foo.123.bar.456.baz.789.geek'

result1 = re.sub(r'\d+', r'#', text)
result2 = re.sub(r'[a-z]+', r'(*)', text)

print(result1)
print(result2)

print('------------------')

import re

result = re.sub(r'(\w+),bar,baz,(\w+)', r'\2,bar,baz,\1', r'foo,bar,baz,qux')

print(result)

print('------------------')

import re

result = re.sub(r'foo,(?P<w1>\w+),(?P<w2>\w+),qux', r'foo,\g<w2>,\g<w1>,qux', r'foo,bar,baz,qux')

print(result)

print('------------------')

import re
def func(match_obj):
    s = match_obj.group(0)         # строка совпадения
    if s.isdigit():
        return str(int(s) * 10)
    else:
        return s.upper()

result = re.sub(r'\w+', func, r'foo.10.bar.20.baz30.40')

print(result)

print('------------------')

import re

text = 'Java самый популярный язык программирования в 2022 году. Язык java — строго типизированный объектно-ориентированный язык программирования общего назначения, разработанный компанией Sun Microsystems. Приложения Java обычно транслируются в специальный байт-код, поэтому они могут работать на любой компьютерной архитектуре, для которой существует реализация виртуальной Java-машины.'

res = re.sub(r'Java', r'Python', text, count=3, flags=re.I)

print(res)

print('------------------')

import re

text = 'foo.123.bar.456.baz.789.geek'

result1 = re.subn(r'\d+', r'#', text)
result2 = re.subn(r'[a-z]+', r'(*)', text, count=2)

print(result1)
print(result2)

print('------------------')

import re
def func(match_obj):
    s = match_obj.group(0)         # строка совпадения
    if s.isdigit():
        return str(int(s) * 10)
    else:
        return s.upper()

result = re.subn(r'\w+', func, 'foo.10.bar.20.baz30.40')

print(result)

print('------------------')

import re

result = re.sub(r'foo,(\w+),(\w+),qux', r'foo,\g<2>,\g<1>,qux', 'foo,bar,baz,qux')

print(result)

print('------------------')

# import re

# result = re.sub(r'(\d+)', r'\10', 'foo 123 bar')

# print(result)

print('------------------')

import re

result = re.sub(r'(\d+)', r'\g<1>0', 'foo 123 bar')

print(result)

print('------------------')

import re

result = re.sub(r'\d+', r'-\g<0>-', 'foo 123 bar 456')

print(result)

print('------------------')

import re

result = re.sub(r'\d+', r'xxx', 'foo bar buz')

print(result)

print('------------------')

import re
a = 'asdad12341 qwe0000 wedas d'
res = re.sub(r'\d+.\d+', print, a)

print('------------------')