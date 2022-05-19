import re
s = input()

while re.search(r'(\d+)\((\w+)\)', s):
    match = re.search(r'(\d+)\((\w+)\)', s)
    a, b = match.span()
    s = s[:a] + match[2] * int(match[1]) + s[b:]

print(s)