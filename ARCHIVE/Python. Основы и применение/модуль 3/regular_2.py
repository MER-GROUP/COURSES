# регулярные выражения
import re
print('-----re-----')
print(re.match)
print(re.search)
print(re.findall)
print(re.sub)

print('-----re.match(pattern, string)-----')
pattern = r'abc'
string = 'abcde'
string_too = 'xyzabcde'
match_object = re.match(pattern, string)
print(match_object)

print('-----re.search(pattern, string_too)-----')
search_object = re.search(pattern, string_too)
print(search_object)

# [] - множество подходящих сисволов
print("-----pattern = r'a[abc]c'-----")
pattern = r'a[abc]c'
match_object = re.match(pattern, 'aac')
print(match_object)
match_object = re.match(pattern, 'abc')
print(match_object)
match_object = re.match(pattern, 'acc')
print(match_object)
match_object = re.match(pattern, 'azc')
print(match_object)

print('-----re.findall(pattern, string)-----')
string = 'abc, aac, acc'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

print("-----.sub(pattern, 'abc', string)-----")
fixed_typos = re.sub(pattern, 'abc', string)
print(fixed_typos)