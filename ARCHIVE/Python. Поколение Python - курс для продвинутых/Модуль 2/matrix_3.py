def matrix_in(n, m):
	arr = [[input() for i in range(m)] for _ in range(n)]
	return arr
	
def matrix_out(arr):
	for i in arr:
		for j in i:
			print(j, end=' ')
		print()
	
if __name__ == '__main__':
	arr = matrix_in(int(input()), int(input()))
	matrix_out(arr)