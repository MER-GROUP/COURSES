class Matrix():
	def __init__(self, n, pow):
		arr = [list(map(int, input().split())) for _ in range(n)]
		# привязывает все объекты
		# к одному значению
		# self.arr = arr.copy()
		# self.power = arr.copy()
		self.arr = [[j for j in i] for i in arr]
		self.power = [[j for j in i] for i in arr]
		self.__matrix_print__()
		#self.__matrix_mult__()
		self.__matrix_pow__(pow)
		#self.__matrix_print__()
		
	def __matrix_print__(self):
		print('*****************************')
		for i in self.arr:
			for j in i:
				print(str(j).ljust(10), end=' ')
			print()
		print('*****************************')
			
	def __matrix_mult__(self):
		arr1 = [[j for j in i] for i in self.arr]
		arr2 = [[j for j in i] for i in self.power]
		# при таком копировании
		# arr1 = self.arr.copy()
		# arr2 = self.power.copy()
		# self.arr[i].clear() очистит у всех
		# ссылочных обьъктов значения
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