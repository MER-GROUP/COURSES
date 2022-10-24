class Matrix:
	def __init__(self, n, m):
		self.arr = [[self.__matrix_alg__(n, m, i, j) for j in range(m)] for i in range(n)]
		self.__matrix_print__()
		
	def __matrix_print__(self):
		for i in self.arr:
			for j in i:
				print(str(j).ljust(3), end=' ')
			print()
			
	def __matrix_alg__(self, n, m, i, j):
		return (i + j) % m + 1
			
if __name__ == '__main__':
	Matrix(*list(map(int, input().split())))