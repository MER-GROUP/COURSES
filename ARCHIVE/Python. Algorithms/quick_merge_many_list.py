def QuickMerge(list1, list2):
	arr = list()
	p1, p2 = int(), int()
	while p1 < len(list1) and p2 < len(list2):
		if list1[p1] <= list2[p2]:
			arr.append(list1[p1])
			p1 += 1
		else:
			arr.append(list2[p2])
			p2 += 1
	if p1 < len(list1):
		arr += list1[p1 : ]
	else:
		arr += list2[p2 : ]
	return arr
	
def QuickMergeLists(arr):
	res = arr[0]
	for i in range(1, len(arr)):
		res = QuickMerge(res, arr[i])
	return res
	
	
digit = int(input())
arr = [[int(i) for i in input().split()] for _ in range(digit)]
#print(arr)
print(*QuickMergeLists(arr))