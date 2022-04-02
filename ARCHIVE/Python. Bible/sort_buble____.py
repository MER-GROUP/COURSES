arr = [6, 9, 0, -4, 3, 55, 2]
print(arr)
for i in range(len(arr) - 1):
	for j in range(len(arr) - 1 - i):
		if arr[j] > arr[j + 1]:
			arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)