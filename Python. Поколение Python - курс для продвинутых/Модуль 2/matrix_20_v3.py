class Matrix:
	def __init__(self, n):
		self.arr = [[(i >= j) + (i > j) for j in range(n)][::-1] for i in range(n)]
		self.__matrix_out__()
		
	def __matrix_out__(self):
		for i in self.arr:
			print(*i)
		
if __name__ == '__main__':
	Matrix(int(input()))