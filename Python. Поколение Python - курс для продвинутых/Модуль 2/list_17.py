def my_list(arr):
	res = [[]]
	for n in range(1, len(arr) + 1):
		for i in range(0, len(arr)):
			if n == len(arr[i : i + n]):
				res.append(arr[i : i + n])
	print(res)
	
if __name__ == '__main__':
	my_list(input().split())