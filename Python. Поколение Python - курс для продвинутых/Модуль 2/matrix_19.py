class Matrix:
	def __init__(self, n, m):
		self.n = n
		self.m = m
		self.arr = [(['.'] * m) for _ in range(n)]
		self.__matrix_in__()
		self.__matrix_out__()
		
	def __matrix_out__(self):
		for i in self.arr:
			print(*i)
			
	def __matrix_in__(self):
		for i in range(self.n):
			for j in range(self.m):
				if 0 == i % 2:
					if 1 == j % 2:
						self.arr[i][j] = '*'
				else:
					if 0 == j % 2:
						self.arr[i][j] = '*'
		
if __name__ == '__main__':
	Matrix(*list(map(int, input().split())))