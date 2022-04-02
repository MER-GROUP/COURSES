class Matrix:
	def __init__(self, n, m):
		self.n, self.m = n, m
		self.arr = ['.', '*'] * n * m
		self.__matrix_out__()
		
	def __matrix_out__(self):
		for i in range(self.n):
			print(*self.arr[i: i + self.m])
		
if __name__ == '__main__':
	Matrix(*list(map(int, input().split())))