class Matrix:
	def __init__(self, n, m):
		self.arr = [input().split() for _ in range(n)]
		self.col1, self.col2 = (map(int, input().split()))
		self.__matrix_cols_rev__()
		self.__matrix_out__()
		
	def __matrix_cols_rev__(self):
		for i in range(len(self.arr)):
			self.arr[i][self.col1], self.arr[i][self.col2] = self.arr[i][self.col2], self.arr[i][self.col1]
			
	def __matrix_out__(self):
		for i in self.arr:
			print(*i)
		
if __name__ == '__main__':
	Matrix(int(input()), int(input()))