def square(n):
	arr = list()
	for i in range(n):
		arr.append(list(range(1, n + 1)))
	print(*arr, sep='\n')
	
if __name__ == '__main__':
	square(int(input()))