a, b = int(input()), int(input())
sum = int()
total = int()
digit = int()

for i in range(a, b + 1):
	sum = 0
	for j in range(1, i + 1):
		if 0 == i % j:
			sum += j
	if not 0 == sum:
		if total <= sum:
			total = sum
			digit = i
	
print(digit, ' ', total, sep='')