class Matrix:
	def __init__(self, n):
		self.arr = [input().split() for _ in range(n)]
		self.__matrix_rotate__()
		self.__matrix_out__()
		
	def __matrix_rotate__(self):
		self.arr.reverse()
				
	def __matrix_out__(self):
		for i in range(len(self.arr)):
			for j in range(len(self.arr)):
				print(self.arr[j][i], end=' ')
			print()
		
if __name__ == '__main__':
	Matrix(int(input()))