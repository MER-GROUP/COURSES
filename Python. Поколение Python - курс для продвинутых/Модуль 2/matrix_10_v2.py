n, m = int(input()), int(input())
for i in range(n):
	print(*[str(i * j).ljust(2) for j in range(m)])