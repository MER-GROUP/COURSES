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

		diag_main = int()
		check = False
		for k in range(-7, 8):
			for i in range(8):
				for j in range(8):
					if i + k == j and 'Q' == self.arr[i][j]:
						diag_main = k
						check = True
						break
				if check:
					break
			if check:
				break
				
		for i in range(8):
			for j in range(8):
				if i + diag_main == j and not 'Q' == self.arr[i][j]:
					self.arr[i][j] = '*'
					
		diag_other = int()
		check = False
		for k in range(-6, 9):
			for i in range(8):
				for j in range(8):
					if 8 == i + j + k and 'Q' == self.arr[i][j]:
						diag_other = k
						check = True
						break
				if check:
					break
			if check:
				break
				
		for i in range(8):
			for j in range(8):
				if 8 == i + j + diag_other and not 'Q' == self.arr[i][j]:
					self.arr[i][j] = '*'
		
if __name__ == '__main__':
	Matrix(input())