class Matrix:
	def __init__(self, n):
		self.arr = [input().split() for _ in range(n)]
		self.__matrix_mirror_gor__()
		self.__matrix_out__()
		
	def __matrix_mirror_gor__(self):
		self.arr.reverse()
			
	def __matrix_out__(self):
		for i in self.arr:
			print(*i)
		
if __name__ == '__main__':
	Matrix(int(input()))