class Matrix:
	def __init__(self, n):
		self.arr = [list(map(int, input().split())) for i in range(n)]
		self.__matrix_alg__()
		
	def __matrix_alg__(self):
		for i in range(len(self.arr)):
			for j in range(len(self.arr)):
				print(self.arr[j][i], end=' ')
			print()
		
if __name__ == '__main__':
	Matrix(int(input()))