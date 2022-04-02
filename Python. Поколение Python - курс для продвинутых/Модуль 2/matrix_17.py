class Matrix:
	def __init__(self, yx):
		self.arr = [['.'] * 8 for _ in range(8)]
		self.yx = yx
		self.y = self.__y__(self.yx)
		self.x = self.__x__(self.yx)
		self.arr[self.x][self.y] = 'N'
		self.__matrix_step__()
		self.__matrix_out__()
		
	def __y__(self, yx):
		cnt = int()
		for i in range(ord('a'), ord('h') + 1):
			cnt += 1
			if yx[0] == chr(i):
				break
		return cnt - 1
		
	def __x__(self, yx):
		return int(yx[1]) - 1
		
	def __matrix_out__(self):
		for i in reversed(self.arr):
			print(*i)
			
	def __matrix_step__(self):
		if self.x + 1 < 8 and self.y - 2 >= 0:
			self.arr[self.x + 1][self.y - 2] = '*'
		if self.x + 1 < 8 and self.y + 2 < 8:
			self.arr[self.x + 1][self.y + 2] = '*'
		if self.x - 1 >= 0 and self.y - 2 >= 0:
			self.arr[self.x - 1][self.y - 2] = '*'
		if self.x - 1 >= 0 and self.y + 2 < 8:
			self.arr[self.x - 1][self.y + 2] = '*'
		
		if self.x + 2 < 8 and self.y - 1 >= 0:
			self.arr[self.x + 2][self.y - 1] = '*'
		if self.x + 2 < 8 and self.y + 1 < 8:
			self.arr[self.x + 2][self.y + 1] = '*'
		if self.x - 2 >= 0 and self.y - 1 >= 0:
			self.arr[self.x - 2][self.y - 1] = '*'
		if self.x - 2 >= 0 and self.y + 1 < 8:
			self.arr[self.x - 2][self.y + 1] = '*'
		
if __name__ == '__main__':
	Matrix(input())