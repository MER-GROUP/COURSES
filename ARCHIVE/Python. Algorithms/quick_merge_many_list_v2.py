def QuickMergeList(arr):
	res = list()
	p = [0] * len(arr)
	step_i, step_min = int(),int()
	while True:
		count = int()
		min = int()
		# псевдо минимум
		for i in range(len(arr)):
			if not p[i] < len(arr[i]):
				count += 1
				continue
			min = arr[i][p[i]]
			step_i = i
			step_min = i
			break
		if count == len(arr):
			break
		# выбор минимома
		while step_i < len(arr):
			if not p[step_i] < len(arr[step_i]):
				step_i += 1
				continue
			if min > arr[step_i][p[step_i]]:
				min = arr[step_i][p[step_i]]
				step_min = step_i
			step_i += 1
		res.append(min)
		p[step_min] += 1
	return res
	
digit = int(input())
arr = [ [int(i) for i in input().split()] for _ in range(digit)]
print(arr)
print(QuickMergeList(arr))