n, m = map(int, input().split())

is_diff = n * m < 0
n, m = abs(n), abs(m)
n, m = min(n, m), max(n, m)

if is_diff:
    print(n * 8 + m * 2)
else:
    print(m * 2)