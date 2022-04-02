class Matrix:
	def __init__(self, n, m):
		self.arr = [[0] * m for i in range(n)]
		self.__matrix_alg__(n, m)
		self.__matrix_print__()
		
	def __matrix_print__(self):
		for i in self.arr:
			for j in i:
				print(str(j).ljust(3), end=' ')
			print()
			
	def __matrix_alg__(self, n, m):
		idx = int()
		for i in range(n):
			for j in range(m):
				idx += 1
				if 0 == i % 2:
					self.arr[i][j] = idx
				else:
					self.arr[i][~j] = idx
			
if __name__ == '__main__':
	Matrix(*list(map(int, input().split())))