def square(n):
	arr = [[i for i in range(1, n + 1)] for _ in range(n)]
	print(*arr, sep='\n')
	
if __name__ == '__main__':
	square(int(input()))