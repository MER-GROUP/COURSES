class Matrix:
	def __init__(self, n, m):
		self.arr = [[0] * m for i in range(n)]
		[[self.__matrix_in__(i, j, n) for i in range(n)] for j in range(m)]
		self.__matrix_out__()
		
	def __matrix_in__(self, i, j, n):
		self.arr[i][j] = j * n + i + 1
		
	def __matrix_out__(self):
		for i in self.arr:
			for j in i:
				print(str(j).ljust(3), end=' ')
			print()
		
if __name__ == '__main__':
	Matrix(*list(map(int, input().split())))