def my_list(n):
	arr = [[j for j in range(1, i + 1)] for i in range(1, n + 1)]
	print(*arr, sep='\n')
	
if __name__ == '__main__':
	my_list(int(input()))