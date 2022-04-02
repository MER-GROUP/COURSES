d = int(input())
for i in range(d):
	if d // 2 + 1 > i:
		for j in range(i + 1):
			print('*', end='')
		print()
	else:
		for j in range(d - i, 0, -1):
			print('*', end='')
		print()