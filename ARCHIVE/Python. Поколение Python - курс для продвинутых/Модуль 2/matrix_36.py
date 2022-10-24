class Matrix:
	def __init__(self, n):
		self.arr = [[self.__matrix_alg__(i, j, n) for j in range(n)] for i in range(n)]
		self.__matrix_print__()
		
	def __matrix_print__(self):
		for i in self.arr:
			print(*i)
		
	def __matrix_alg__(self, i, j, n):
		if i == j:
			return '*'
		elif n == i + j + 1:
			return '*'
		elif n // 2 == i:
			return '*'
		elif n // 2 == j:
			return '*'
		else:
			return '.'
		
if __name__ == '__main__':
	Matrix(int(input()))