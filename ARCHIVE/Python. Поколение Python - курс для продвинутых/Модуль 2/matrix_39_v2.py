class Matrix:
	def __init__(self, s):
		self.arr = [ ['.'] * 8 for i in range(8)]
		self.y = 8 - int(s[1])
		self.x = ord(s[0]) - ord('a')
		self.arr[self.y][self.x] = 'Q'
		self.__matrix_alg__()
		self.__matrix_print__()
		
	def __matrix_print__(self):
		for i in self.arr:
			print(*i)
		
	def __matrix_alg__(self):
		check = False
		for i in range(8):
			for j in range(8):
				if i == self.y and not 'Q' == self.arr[i][j]:
					self.arr[i][j] = '*'
				if j == self.x and not 'Q' == self.arr[i][j]:
					self.arr[i][j] = '*'
				if abs(i - self.y) == abs(j - self.x) and not 'Q' == self.arr[i][j]:
					self.arr[i][j] = '*'
		
if __name__ == '__main__':
	Matrix(input())