import numpy as np

class Matrix:
	def __init__(self, n):
		self.arr = [list(map(int, input().split())) for _ in range(n)]
		self.res = list()
		self.np_arr = np.matrix(self.arr)
		self.np_res = np.matrix(self.res)
		self.pow = int(input())
		self.__matrix_pow__()
		self.__matrix_print__()
		
	def __matrix_print__(self):
		for i in self.np_res.tolist():
			print(*i)
					
	def __matrix_pow__(self):
		self.np_res = self.np_arr ** self.pow
		
if __name__ == '__main__':
	Matrix(int(input()))