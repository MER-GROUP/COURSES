n, k = (int(input()) for _ in range(2))
arr = [i for i in range(1,n + 1)]

while 1 != len(arr):
	for i in range(k - 1):
		arr.append(arr.pop(0))
	arr.remove(arr[0])

print(*arr)