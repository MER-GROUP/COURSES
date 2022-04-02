arr = [int(i) for i in input().split()]
count = int()
arrLink = arr
for i in range(len(arr)):
	for j in range(len(arrLink)):
		if arrLink[j] == arr[i] and j != i:
			count += 1
print(int(count / 2))