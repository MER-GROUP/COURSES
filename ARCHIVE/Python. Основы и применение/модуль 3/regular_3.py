# регулярные выражения
import re

# метасимвол ?
print('-----metasymbol: ? -----')
pattern = r'english?'
string = 'Do you speak english?'
match = re.search(pattern, string)
print(match)

pattern = r'english\?'
string = 'Do you speak english?'
match = re.search(pattern, string)
print(match)

# . ^ $ * + ? {} [] \ | () метасимволы
# \d цифры [0-9]
# \D кроме цифр [^0-9]
# \s пробельные (непечатаемые символы) символы [ \t\r\n\f\n]
# \S кроме пробельных (непечатаемых) символов [^ \t\r\n\f\n]
# \w буквы+цивры+_ [a-zA-Z0-9_]
# \W кроме букв+цифр+_ [^a-zA-Z0-9_]

# [] - множество подходящих символов
print("-----pattern = r'a[a-zA-Z]c'-----")
pattern = r'a[a-zA-Z]c'

print('-----re.findall(pattern, string)-----')
string = 'abc, aac, acc, aMc'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

print("-----.sub(pattern, 'abc', string)-----")
fixed_typos = re.sub(pattern, 'abc', string)
print(fixed_typos)

# метасимвол ^
print("-----pattern = r'a[^a-zA-Z]c'-----")
pattern = r'a[^a-zA-Z]c'

print('-----re.findall(pattern, string)-----')
string = 'abc, aac, acc, a&c'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

print("-----.sub(pattern, 'abc', string)-----")
fixed_typos = re.sub(pattern, 'abc', string)
print(fixed_typos)

# группа метасимволов \W
print("-----pattern = r'a[\W]c'-----")
pattern = r'a[\W]c'

print('-----re.findall(pattern, string)-----')
string = 'abc, aac, acc, a&c'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

print("-----.sub(pattern, 'abc', string)-----")
fixed_typos = re.sub(pattern, 'abc', string)
print(fixed_typos)

# метасимвол . (все символы кроме переноса строки)
print("-----pattern = r'a.c'-----")
pattern = r'a.c'

print('-----re.findall(pattern, string)-----')
string = 'abc, aac, acc, a&c'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

print("-----.sub(pattern, 'abc', string)-----")
fixed_typos = re.sub(pattern, 'abc', string)
print(fixed_typos)