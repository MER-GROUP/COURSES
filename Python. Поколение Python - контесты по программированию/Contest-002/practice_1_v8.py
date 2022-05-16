n, result = int(input()), []
i, j = 1, 1
while i <= n:
    result.extend(range(i + j - 1, i - 1, -1))
    i += j
    j += 1
print(*result[:n])