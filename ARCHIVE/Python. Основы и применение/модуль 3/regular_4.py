import re

# метасимвол * (любое число символа включая 0)
print('-----metasymbol * -----')
pattern = r'ab*a'
string = 'aa, aba, abba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

# метасимвол + (любое число символа кроме 0)
print('-----metasymbol + -----')
pattern = r'ab+a'
string = 'aa, aba, abba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

# метасимвол ? (0 или 1 вхождений символа)
print('-----metasymbol ? -----')
pattern = r'ab?a'
string = 'aa, aba, abba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

# метасимвол {} (конкретное число вхождений или отрезок вхождений символа)
print('-----metasymbol {} -----')
pattern = r'ab{2}a'
string = 'aa, aba, abba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r'ab{2,3}a'
string = 'aa, aba, abba, abbba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

# метасимволы [] и + (жадный метод)
print('-----metasymbol [] and + -----')
pattern = r'a[ab]+a'
string = 'abaaba'
match = re.match(pattern, string)
print(match)
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

# метасимволы [] и + и ? (не жадный метод)
print('-----metasymbol [] and + and ? -----')
pattern = r'a[ab]+?a'
string = 'abaaba'
match = re.match(pattern, string)
print(match)
all_inclusions = re.findall(pattern, string)
print(all_inclusions)