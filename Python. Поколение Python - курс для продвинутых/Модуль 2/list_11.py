def square(n):
	for i in range(1, n + 1):
		arr = list()
		for j in range(1, n + 1):
			arr.append(j)
		print(arr)
	
if __name__ == '__main__':
	square(int(input()))