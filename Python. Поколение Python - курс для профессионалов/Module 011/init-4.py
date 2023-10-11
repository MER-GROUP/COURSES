print('------------------')

import re

match1 = re.search('a+', 'aaaAAA')
match2 = re.search('A+', 'aaaAAA')
match3 = re.search('a+', 'aaaAAA', re.IGNORECASE)
match4 = re.search('A+', 'aaaAAA', re.I)

print(match1)
print(match2)
print(match3)
print(match4)

print('------------------')

import re

match1 = re.search('[a-z]+', 'aBcDeF')
match2 = re.search('[a-z]+', 'aBcDeF', re.I)

print(match1)
print(match2)

print('------------------')

import re

text = 'foo\nbar\nbaz'

print(re.search('^foo', text))
print(re.search('^bar', text))
print(re.search('^baz', text))
print(re.search('foo$', text))
print(re.search('bar$', text))
print(re.search('baz$', text))

print('------------------')

import re

text = 'foo\nbar\nbaz'

print(re.search('^foo', text, re.MULTILINE))
print(re.search('^bar', text, re.MULTILINE))
print(re.search('^baz', text, re.MULTILINE))
print(re.search('foo$', text, re.M))
print(re.search('bar$', text, re.M))
print(re.search('baz$', text, re.M))

print('------------------')

import re

text = 'foo\nfoo\nbaz'

print(re.search('^foo', text, re.MULTILINE))
print(re.search('^bar', text, re.MULTILINE))
print(re.search('^baz', text, re.MULTILINE))
print(re.search('foo$', text, re.M))
print(re.search('bar$', text, re.M))
print(re.search('baz$', text, re.M))

print('------------------')

import re

print(re.search('foo.bar', 'foo\nbar'))
print(re.search('foo.bar', 'foo\nbar', re.DOTALL))
print(re.search('foo.bar', 'foo\nbar', re.S))

print('------------------')

import re

match = re.search('^bar', 'FOO\nBAR\nBAZ', re.I | re.M)

print(match)

print('------------------')

from re import escape

print(escape('http://www.stepik.org'))

print('------------------')

from re import escape

operators = ['+', '-', '*', '/', '**']
print(','.join(map(escape, operators)))

print('------------------')

import re

print(re.search('x[123]{2,4}y', 'x222y', re.DEBUG))

print('------------------')

print(int(re.I | re.M))
print(int(re.I + re.M))

print('------------------')