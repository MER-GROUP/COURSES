a, b = int(input()), int(input())

for i in range(a, b + 1):
	if 1 == i:
		continue
	count = 0
	for j in range(1, i + 1):
		if 0 == i % j:
			count += 1
	if 2 == count:
		print(i)