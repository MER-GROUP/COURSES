class Matrix:
	def __init__(self, n, m):
		self.arr1 = [list(map(int, input().split())) for _ in range(n)]
		input()
		self.arr2 = [list(map(int, input().split())) for _ in range(n)]
		self.res = [[0] * m for _ in range(n)]
		self.__matrix_sum__(n, m)
		self.__matrix_print__()
		
	def __matrix_print__(self):
		for i in self.res:
			print(*i)
		
	def __matrix_sum__(self, n, m):
		for i in range(n):
			for j in range(m):
				self.res[i][j] = self.arr1[i][j] + self.arr2[i][j]
		
if __name__ == '__main__':
	Matrix(*list(map(int, input().split())))