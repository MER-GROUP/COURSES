arr = [int(i) for i in input().split()]
count = int()
tempArr = list()
for i in arr:
	if i in arr and 1 < arr.count(i):
		for j in range(arr.count(i)):
			tempArr.append(i)
			arr.remove(i)
		for j in range(len(tempArr)):
			for k in range(len(tempArr) - j):
				count += 1
			count -= 1
		tempArr.clear()
print(count)