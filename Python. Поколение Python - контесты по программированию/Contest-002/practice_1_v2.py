# авторское решение
n = int(input())
index, count = 1, 1
result = []
while(len(result) < n):
    result += range(index, index-count, -1)
    count += 1
    index += count
print(*result[:n])