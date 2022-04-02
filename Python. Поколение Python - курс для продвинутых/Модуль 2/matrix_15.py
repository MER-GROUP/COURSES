class Matrix:
	def __init__(self, n):
		self.arr = [input().split() for _ in range(n)]
		self.__matrix_mirror_gor__()
		self.__matrix_out__()
		
	def __matrix_mirror_gor__(self):
		for i in range(len(self.arr)):
			for j in range(len(self.arr)):
				self.arr[i][j], self.arr[len(self.arr) - i - 1][j] = self.arr[len(self.arr) - i - 1][j], self.arr[i][j]
			if i >= (len(self.arr) - 1) // 2:
				break
			
	def __matrix_out__(self):
		for i in self.arr:
			print(*i)
		
if __name__ == '__main__':
	Matrix(int(input()))