d = int(input())
for i in range(d):
	for j in range(i + 1):
		print(i + 1, end='')
	print()
	
d = int(input())
for i in range(1, d + 1):
	print(str(i) * i, end='')
	print()
	
d = int(input())
for i in range(1, d + 1):
	for j in range(1, d + 1):
		if j == i:
			print(str(j) * j, end='')
	print()