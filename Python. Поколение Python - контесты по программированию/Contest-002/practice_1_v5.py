n = int(input())

i = 1
j = 1

while n > 0:
    for k in range(j + i - 1, j - 1, -1):
        if n == 0:
            break
        print(k, end=" ")
        n -= 1
    j += i
    i += 1

print()