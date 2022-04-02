class Matrix:
	def __init__(self, n):
		self.arr = list()
		if n % 2:
			print('Матрица должна быть четной')
			exit()
		else:
			self.arr = [[self.__matrix_alg__(i, j, n) for j in range(n)] for i in range(n)]
		self.__matrix_pic__(n)
		self.__matrix_print__()
			
	def __matrix_print__(self):
			for i in self.arr:
				print(*i)
			
	def __matrix_alg__(self, i, j, n):
		if i < n / 2 and j < n / 2:
			return 1
		if i < n / 2 and j >= n / 2:
			return 2
		if i >= n / 2 and j >= n / 2:
			return 3
		if i >= n / 2 and j < n / 2:
			return 4
			
	def __matrix_pic__(self, n):
		for i in range(n):
			for j in range(n):
				self.arr[i][i] = '*'
				self.arr[i][~i] = '*'
				if int(n / 2) == i + j + 1:
					self.arr[i][j] = '*'
				if int(n / 2) + n == i + j + 1:
					self.arr[i][j] = '*'
				if i + int(n / 2) == j:
					self.arr[i][j] = '*'
				if i - int(n / 2) == j:
					self.arr[i][j] = '*'
		
if __name__ == '__main__':
	Matrix(int(input()))