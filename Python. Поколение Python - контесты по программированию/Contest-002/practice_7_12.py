import re
s = input()

while '(' in s:
    # ищем самую маленькую подстроку для замены
    sample = re.search(r'[\d]+[(]\w*[)]', s)
    start = sample.start()
    end = sample.end()

    # ищем число в подстроке
    st = sample.group()
    n = int(re.search(r'[\d]+', st).group())

    substr = s[start + 1 + len(str(n)):end-1]
    s = s[:start] + n * substr + s[end:]
print(s)