print('------------------')

import re

regex_obj = re.compile('\d+')
text = 'ул. Часовая, дом № 25, корпус 2, квартира 69'
result = re.findall(regex_obj, text)

print(result)

print('------------------')

import re

regex_obj = re.compile('\d+')
text = 'ул. Часовая, дом № 25, корпус 2, квартира 69'
result = regex_obj.findall(text)

print(result)

print('------------------')

import re

regex_obj = re.compile('ba[rz]', flags=re.I)

result1 = re.search('ba[rz]', 'FOOBARBAZ', flags=re.I)
result2 = re.search(regex_obj, 'FOOBARBAZ')
result3 = regex_obj.search('FOOBARBAZ')

print(result1)
print(result2)
print(result3)

print('------------------')

import re

s1, s2, s3, s4 = 'foo.bar', 'foo123bar', 'baz99', 'qux & grault'

print(re.search('\d+', s1))
print(re.search('\d+', s2))
print(re.search('\d+', s3))
print(re.search('\d+', s4))

print('------------------')

import re

s1, s2, s3, s4 = 'foo.bar', 'foo123bar', 'baz99', 'qux & grault'

regex_obj = re.compile('\d+')

print(regex_obj.search(s1))
print(regex_obj.search(s2))
print(regex_obj.search(s3))
print(regex_obj.search(s4))

print('------------------')

import re

regex_obj = re.compile('\d+')
text = 'foo12345barbaz'

print(regex_obj.search(text))
print(regex_obj.search(text, pos=4))
print(regex_obj.search(text, endpos=7))
print(regex_obj.search(text, pos=4, endpos=7))

print('------------------')

import re

regex_obj = re.compile('\d')

print(type(regex_obj))

print('------------------')