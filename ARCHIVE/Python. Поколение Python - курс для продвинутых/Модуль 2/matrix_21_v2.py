class Matrix:
	def __init__(self, n, m):
		self.arr = [[self.__matrix_in__(i, j, m) for j in range(m)] for i in range(n)]
		self.__matrix_out__()
		
	def __matrix_out__(self):
		for i in self.arr:
			for j in i:
				print(str(j).ljust(3), end=' ')
			print()
		
	def __matrix_in__(self, i, j, m):
		return i * m + j + 1
		
if __name__ == '__main__':
	Matrix(*list(map(int, input().split())))