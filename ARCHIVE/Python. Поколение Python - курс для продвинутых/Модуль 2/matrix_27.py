class Matrix:
	def __init__(self, n, m):
		self.arr = [[0] * m for i in range(n)]
		self.it = iter(range(1, (n * m) + 1))
		self.__matrix_alg__(n, m, self.it)
		self.__matrix_print__()
		
	def __matrix_print__(self):
		for i in self.arr:
			for j in i:
				print(str(j).ljust(3), end=' ')
			print()
			
	def __matrix_alg__(self, n, m, it):
		for k in range(1, n + m):
			for i in range(n):
				for j in range(m):
					if k == i + j + 1:
						self.arr[i][j] = next(it)
		
if __name__ == '__main__':
	Matrix(*list(map(int, input().split())))