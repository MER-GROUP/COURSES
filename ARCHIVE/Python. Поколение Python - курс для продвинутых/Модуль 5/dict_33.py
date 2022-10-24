numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

def deliteli(n):
	arr = list()
	for i in range(1, n + 1):
		if 0 == n % i:
			arr.append(i)
	return  arr

result = {i: deliteli(i) for i in sorted(numbers)}
print(result)