class Matrix:
	def __init__(self, n):
		self.arr = [list(map(int, input().split())) for i in range(n)]
		self.__matrix_alg__()
		
	def __matrix_alg__(self):
		max = self.arr[len(self.arr) - 1][0]
		for i in range(len(self.arr)):
			for j in range(len(self.arr)):
				if i + j + 1 >= len(self.arr):
					if max < self.arr[i][j]:
						max = self.arr[i][j]
		print(max)
		
if __name__ == '__main__':
	Matrix(int(input()))