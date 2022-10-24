from copy import deepcopy

class Matrix:
	def __init__(self, n):
		self.arr = [list(map(int, input().split())) for _ in range(n)]
		self.arr_pow = deepcopy(self.arr)
		self.res = [[0] * len(self.arr_pow[0]) for _ in range(len(self.arr))]
		self.pow = int(input())
		self.__matrix_pow__()
		self.__matrix_print__()
		
	def __matrix_print__(self):
		for i in self.arr:
			print(*i)
			
	def __matrix_mult(self, arr1, arr2):
		for i in range(len(arr1)):
			for k in range(len(arr2[0])):
				for j in range(len(arr2)):
					# print(f'arr1[i][j] = {arr1[i][j]}, arr2[j][k] = {arr2[j][k]}')
					self.res[i][k] += arr1[i][j] * arr2[j][k]
		self.arr = deepcopy(self.res)
		self.res = [[0] * len(self.arr_pow[0]) for _ in range(len(self.arr))]
					
	def __matrix_pow__(self):
		for i in range(self.pow - 1):
			self.__matrix_mult(self.arr, self.arr_pow)
		
if __name__ == '__main__':
	Matrix(int(input()))