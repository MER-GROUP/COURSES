import copy

class Matrix():
	def __init__(self, n, pow):
		arr = [list(map(int, input().split())) for _ in range(n)]
		self.arr = copy.deepcopy(arr)
		self.power = copy.deepcopy(arr)
		self.__matrix_print__()
		self.__matrix_pow__(pow)
		
	def __matrix_print__(self):
		print('*****************************')
		for i in self.arr:
			for j in i:
				print(str(j).ljust(10), end=' ')
			print()
		print('*****************************')
			
	def __matrix_mult__(self):
		arr1 = copy.deepcopy(self.arr)
		arr2 = copy.deepcopy(self.power)
		for i in range(len(arr1)):
			self.arr[i].clear()
			j = int()
			cnt = int()
			while True:
				for x in range(len(arr2[0])):
					sum = int()
					for y in range(len(arr2)):
						sum += arr1[i][j] * arr2[y][x]
						j += 1
						if len(arr1[0]) == j:
							j = 0
							cnt += 1
					self.arr[i].append(sum)
					# print(sum)
				if len(arr1[0]) <= cnt:
					break
					
	def __matrix_pow__(self, pow):
		for _ in range(pow - 1):
			self.__matrix_mult__()
			self.__matrix_print__()
		
if __name__ == '__main__':
	Matrix(*list(map(int, input().split())))