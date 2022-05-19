from re import subn

rex = r'(\d+)\((\w+)\)'
text = input()
flag = True

while flag:
    text, flag = subn(rex, lambda m: int(m.group(1)) * m.group(2), text)

print(text)