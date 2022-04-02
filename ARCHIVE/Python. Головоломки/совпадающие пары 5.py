arr = [int(i) for i in input().split()]
count = int()
for i in range(len(arr)):
	count += arr[i + 1 : ].count(arr[i])
print(count)