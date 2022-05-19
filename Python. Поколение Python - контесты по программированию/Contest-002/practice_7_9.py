import re

txt = input()
while '(' in txt:
    find = re.findall(r'\d+\([a-z]+?\)', txt)
    for part in sorted(find, key=lambda x: -int(x.split('(')[0])):
        n = re.search(r'\d+', part)[0]
        s = re.search(r'[a-z]+', part)[0]
        txt = txt.replace(part, int(n) * s)
print(txt)