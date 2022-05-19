s = input()
while ")" in s:
    r = s.index(")")
    l = 0
    n = ""
    for i in range(r - 1, -1, -1):
        if s[i] == "(":
            l = i
            break
    k = l - 1
    while s[k:l].isdigit():
        k -= 1
    k += 1
    sub = s[k:r + 1]
    rep = int(s[k:l]) * s[l + 1:r]
    s = s.replace(sub, rep)
print(s)