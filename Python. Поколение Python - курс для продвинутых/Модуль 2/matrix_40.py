class Matrix:
	def __init__(self, n):
		self.arr = [ ['.'] * n for i in range(n)]
		self.n = n
		self.__matrix_alg__()
		self.__matrix_print__()
		
	def __matrix_print__(self):
		for i in self.arr:
			print(*i)
		
	def __matrix_alg__(self):
		for i in range(self.n):
			for j in range(self.n):
				self.arr[i][j] = abs(i - j)
		
if __name__ == '__main__':
	Matrix(int(input()))