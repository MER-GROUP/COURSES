class Matrix:
	def __init__(self, n, m):
		self.idx = int()
		self.arr = [[self.__matrix_in__() for _ in range(m)] for _ in range(n)]
		self.__matrix_out__()
		
	def __matrix_out__(self):
		for i in self.arr:
			for j in i:
				print(str(j).ljust(3), end=' ')
			print()
		
	def __matrix_in__(self):
		self.idx += 1
		return self.idx
		
if __name__ == '__main__':
	Matrix(*list(map(int, input().split())))