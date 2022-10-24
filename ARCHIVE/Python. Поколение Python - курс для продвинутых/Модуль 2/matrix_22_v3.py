class Matrix:
	def __init__(self, n, m):
		self.arr = [list(range(i + 1, n * m + i + 1, n)) for i in range(n)]
		self.__matrix_out__()
		
	def __matrix_out__(self):
		for i in self.arr:
			for j in i:
				print(str(j).ljust(3), end=' ')
			print()
		
if __name__ == '__main__':
	Matrix(*list(map(int, input().split())))