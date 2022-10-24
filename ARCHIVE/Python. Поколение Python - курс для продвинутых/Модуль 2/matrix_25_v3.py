class Matrix:
	def __init__(self, n, m):
		self.arr = [[0] * m for i in range(n)]
		self.__matrix_alg__(n, m)
		self.__matrix_print__()
		
	def __matrix_print__(self):
		for i in self.arr:
			for j in i:
				print(str(j).ljust(3), end=' ')
			print()
			
	def __matrix_alg__(self, n, m):
		tmp = [int(k) for k in range(1, m + 1)]
		for i in range(n):
			self.arr[i] = tmp.copy()
			tmp = tmp[1 : ] + tmp[ : 1]
			
if __name__ == '__main__':
	Matrix(*list(map(int, input().split())))