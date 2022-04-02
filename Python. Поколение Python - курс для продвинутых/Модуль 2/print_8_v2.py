n, k = (int(input()) for _ in range(2))
killer = int()
for i in range(1, n + 1):
	killer = (killer + k) % i
print(killer + 1)