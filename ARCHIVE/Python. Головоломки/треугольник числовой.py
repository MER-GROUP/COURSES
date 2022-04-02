d = int(input())
count = 1
for i in range(1, d + 1):
	print(*range(count, i + count))
	count += 1
	
d = int(input())
count = int(1)
for i in range(1, d + 1):
	for j in range(i):
		print(count, end=' ')
		count += 1
	print()