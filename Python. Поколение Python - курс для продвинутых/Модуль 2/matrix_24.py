class Matrix:
	def __init__(self, n):
		self.arr = [[self.__matrix_in__(i, j, n) for j in range(n)] for i in range(n)]
		self.__matrix_out__()
		
	def __matrix_in__(self, i, j, n):
		if j >= i and n >= i + j + 1 or j <= i and n <= i + j + 1:
			return 1
		else:
			return 0
		
	def __matrix_out__(self):
		for i in self.arr:
			for j in i:
				print(str(j).ljust(3), end=' ')
			print()
		
if __name__ == '__main__':
	Matrix(int(input()))