def sublist(arr, n):
	res = list()
	for i in range(len(arr) - n + 1):
			res.append(arr[i : i + n])
	return res
	
if __name__ == '__main__':
	arr = [[]]
	s = input().split()
	for i in range(1, len(s) + 1):
		arr.extend(sublist(s, i))
	print(arr)