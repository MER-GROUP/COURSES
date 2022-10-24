class Matrix:
	def __init__(self, n):
		self.arr = [[self.__matrix_in__() for j in range(n)] for i in range(n)]
		self.__matrix_diag__()
		self.__matrix_out__()
		
	def __matrix_in__(self):
		return 0
		
	def __matrix_diag__(self):
		for i in range(len(self.arr)):
			self.arr[i][i] = 1
			self.arr[i][~i] = 1
		
	def __matrix_out__(self):
		for i in self.arr:
			for j in i:
				print(str(j).ljust(3), end=' ')
			print()
		
if __name__ == '__main__':
	Matrix(int(input()))