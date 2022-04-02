class Matrix:
	def __init__(self, n, x, y):
		self.arr = list()
		if n % 2:
			print('Матрица должна быть четной')
			exit()
		else:
			self.arr = [[self.__matrix_alg__(i, j, n) for j in range(n)] for i in range(n)]
			self.arr[y - 1][ x - 1] = 'M'
		self.__matrix_pic__(n, x, y)
		self.__matrix_print__()
			
	def __matrix_print__(self):
			for i in self.arr:
				print(*i)
			
	def __matrix_alg__(self, i, j, n):
		return '.'
			
	def __matrix_pic__(self, n, x, y):
		for i in range(n):
			for j in range(n):
				if x + y - 1 == i + j + 1 and not 'M' == self.arr[i][j]:
					self.arr[i][j] = '*'
				if i + (x - y) == j and not 'M' == self.arr[i][j]:
					self.arr[i][j] = '*'
				if y - 1 == i and not 'M' == self.arr[i][j]:
					self.arr[i][j] = '*'
				if x - 1 == j and not 'M' == self.arr[i][j]:
					self.arr[i][j] = '*'
		
if __name__ == '__main__':
	Matrix(*list(map(int, input().split())))