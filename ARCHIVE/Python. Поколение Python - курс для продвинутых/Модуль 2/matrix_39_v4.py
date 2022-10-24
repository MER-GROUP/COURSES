class Matrix:
	def __init__(self, s):
		self.arr = [ ['.'] * 8 for i in range(8)]
		self.y = 8 - int(s[1])
		self.x = ord(s[0]) - ord('a')
		self.__matrix_alg__()
		self.__matrix_print__()
		
	def __matrix_print__(self):
		for i in self.arr:
			print(*i)
		
	def __matrix_alg__(self):
		left = self.x - self.y
		right = self.x + self.y
		for i in range(8):
			self.arr[i][self.x] = '*'
			self.arr[self.y][i] = '*'
			if 0 < self.y - i and 0 < self.x - i:
				self.arr[self.y - i - 1][self.x - i - 1] = '*'
			if 0 < self.y - i and 7 > self.x + i:
				self.arr[self.y - i - 1][self.x + i +1] = '*'
			if 7 > self.y + i and 7 > self.x + i:
				self.arr[self.y + i + 1][self.x + i +1] = '*'
			if 7 > self.y + i and 0 < self.x - i:
				self.arr[self.y + i + 1][self.x - i -1] = '*'
		self.arr[self.y][self.x] = 'Q'
		
if __name__ == '__main__':
	Matrix(input())