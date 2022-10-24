class Matrix:
	def __init__(self, n):
		self.arr = [[self.__matrix_in__(i, j, n) for j in range(n)] for i in range(n)]
		self.__matrix_out__()
		
	def __matrix_out__(self):
		for i in self.arr:
			print(*i)
			
	def __matrix_in__(self, i, j, n):
		if i == n - j - 1:
			return 1
		elif n > i + j + 1:
			return 0
		else:
			return 2
		
if __name__ == '__main__':
	Matrix(int(input()))