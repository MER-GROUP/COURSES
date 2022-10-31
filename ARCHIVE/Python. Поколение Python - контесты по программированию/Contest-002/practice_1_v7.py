n, s, l = int(input()), [1], 1

while len(s) < n:
    l += 1
    a = sorted(s)[-1] + 1
    s += list(range(a, a+l))[::-1]

print(*s[:n])