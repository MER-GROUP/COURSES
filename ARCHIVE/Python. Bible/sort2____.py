arr = [5, 7, 0, 3 ,1, 7 ,4, 55]
count = int()
for i in range(len(arr)):
	for j in range(i):
		count += 1
		if arr[j] > arr[i]:
			arr[j], arr[i] = arr[i], arr[j]
print(arr)

count2 = int()
arr = [5, 7, 0, 3 ,1, 7 ,4, 55]
for i in range(len(arr) - 1):
	for j in range(len(arr) - i -1):
		count2 += 1
		if arr[j] > arr[j + 1]:
			arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)

print(count)
print(count2)