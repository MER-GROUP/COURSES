class Matrix:
	def __init__(self, n):
		self.arr = [[0 for _ in range(n - i - 1)] + [1] + [2 for _ in range(i)] for i in range(n)]
		self.__matrix_out__()
		
	def __matrix_out__(self):
		for i in self.arr:
			print(*i)
		
if __name__ == '__main__':
	Matrix(int(input()))