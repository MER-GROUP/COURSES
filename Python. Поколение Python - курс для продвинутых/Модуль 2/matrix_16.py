class Matrix:
	def __init__(self, n):
		self.arr = [input().split() for _ in range(n)]
		# неверно работает
		#self.res = self.arr.copy()
		# self.res = list(self.arr)
		# self.res = [[0] * n] * n
		# работает
		self.res = [[0] * n for _ in range(n)]
		self.__matrix_rotate__()
		self.__matrix_out__()
		
	def __matrix_rotate__(self):
		for i in range(len(self.arr)):
			for j in range(len(self.arr)):
				self.res[j][i] = self.arr[len(self.arr) - i - 1][j]
				
	def __matrix_out__(self):
		for i in self.res:
			print(*i)
		
if __name__ == '__main__':
	Matrix(int(input()))