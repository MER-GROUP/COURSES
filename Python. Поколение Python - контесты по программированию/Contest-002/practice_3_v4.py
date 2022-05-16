n, m = (int(x) for x in input().split())
print(8 * int(n * m < 0) * min(abs(n), abs(m)) + 2 * max(abs(n), abs(m)))