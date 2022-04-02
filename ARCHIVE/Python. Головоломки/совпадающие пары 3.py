arr = [int(i) for i in input().split()]
count = int()
for i in range(len(arr) - 1):
	for j in range(i + 1, len(arr)):
		if arr[j] == arr[i]:
			count += 1
print(count)