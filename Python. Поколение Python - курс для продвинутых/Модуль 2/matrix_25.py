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
		for i in range(n):
			idx = 1
			for j in range(m):
				if m >= n:
					if m < i + j + 1:
						self.arr[i][j] = idx
						idx += 1
					else:
						self.arr[i][j] = i + j + 1
				elif m < n:
					if m >= i + j + 1:
						self.arr[i][j] = i + j + 1
					elif n >= i + j + 1:
						if  i <= m:
							self.arr[i][j] = idx
							idx += 1
						else:
							self.arr[i][j] = self.arr[i - m][j]
					else:
						self.arr[i][j] = self.arr[i - m][j]
			
if __name__ == '__main__':
	Matrix(*list(map(int, input().split())))