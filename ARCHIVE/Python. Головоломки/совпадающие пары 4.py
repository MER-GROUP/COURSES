arr = [int(i) for i in input().split()]
count = int()
while 1 < len(arr):
	if 1 < arr.count(arr[0]):
		count += arr.count(arr[0]) - 1
	del arr[0]
print(count)