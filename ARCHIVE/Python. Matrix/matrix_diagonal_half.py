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
				if i < y and j < x and not 'M' == self.arr[i][j]:
					self.arr[i][j] = '+'
				if i < y and j >= x and not 'M' == self.arr[i][j]:
					self.arr[i][j] = '-'
				if i >= y and j < x and not 'M' == self.arr[i][j]:
					self.arr[i][j] = '='
				if i >= y and j >= x and not 'M' == self.arr[i][j]:
					self.arr[i][j] = '^'
					
				if 0 <= y - j - 1 and 0 <= x - j - 1 and not 'M' == self.arr[y - j -1][x - j - 1]:
					self.arr[y - j -1][x - j - 1] = 'x'
				if 0 <= y - j - 1 and n > x + j - 1 and not 'M' == self.arr[y - j -1][x + j - 1]:
					self.arr[y - j -1][x + j - 1] = 'v'
				if n > y + j - 1 and n > x + j - 1 and not 'M' == self.arr[y + j -1][x + j - 1]:
					self.arr[y + j -1][x + j - 1] = 'u'
				if n > y + j - 1 and 0 <= x - j - 1 and not 'M' == self.arr[y + j -1][x - j - 1]:
					self.arr[y + j -1][x - j - 1] = 's'
		
if __name__ == '__main__':
	Matrix(*list(map(int, input().split())))