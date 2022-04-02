# регулярные выражения
import re

# мета символ () группировка выражений
print('-----metasymbol () -----')
pattern = r'(test)*'
string = 'testtest'
match = re.match(pattern, string)
print(match)

# мета символ | или
print('-----metasymbol | -----')
pattern = r'((abc)|(test|text)*)'
#string = 'abc'
string = 'testtexttest'
match = re.match(pattern, string)
print(match)
print(match.groups())

# мета символ | или
print('-----metasymbol | -----')
pattern = r'Hello (abc|test)'
string = 'Hello test'
match = re.match(pattern, string)
print(match)
print(match.groups())
print(match.group())
print(match.group(0))
print(match.group(1))

# мета символ (\w+)-\1 найди группу которую собрал ранее
print('-----metasymbol () and \w and + and 1 -----')
pattern = r'(\w+)-\1'
string = 'test-test chow-chow'
#string = 'test-text'
match = re.match(pattern, string)
print(match)
find = re.findall(pattern, string)
print(find)

# мета символ (\w+)-\1 найди группу которую собрал ранее
print('-----metasymbol () and \w and + and 1 -----')
pattern = r'(\w+)-\1'
string = 'test-test chow-chow'
dublicates = re.sub(pattern, r'\1', string)
print(dublicates)

# мета символ (\w+)-\1 найди группу которую собрал ранее
print('-----metasymbol () and \w and + and 1 -----')
pattern = r'((\w+)-\2)'
string = 'test-test chow-chow'
find = re.findall(pattern, string)
print(find)