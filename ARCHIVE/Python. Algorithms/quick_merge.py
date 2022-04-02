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

list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
print(QuickMerge(list1, list2))