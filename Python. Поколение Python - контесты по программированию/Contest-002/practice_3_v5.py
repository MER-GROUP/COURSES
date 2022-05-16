n, m = map(int, input().split())
if n * m > 0:
    print(max(abs(n), abs(m)) * 2)
else:
    n, m = abs(n), abs(m)
    print((n * 2 + (n * 2 + m)) * 2)