class Matrix:
	def __init__(self, n):
		self.arr = [([0] * n) for _ in range(n)]
		self.__matrix_in__()
		self.__matrix_out__()
		
	def __matrix_out__(self):
		for i in self.arr:
			print(*i)
			
	def __matrix_in__(self):
		for i in range(len(self.arr)):
			self.arr[i][len(self.arr) - i - 1] = 1
			for j in range(len(self.arr)):
				if len(self.arr) < (i + j + 1):
					self.arr[i][j] = 2
		
if __name__ == '__main__':
	Matrix(int(input()))