class Matrix:
	def __init__(self, n=0):
		self.my_dict = {'Верхняя четверть': int(), 'Правая четверть': int(), 'Нижняя четверть': int(), 'Левая четверть': int()}
		self.arr = [list(map(int, input().split())) for _ in range(n)]
		self.__sum_chetvert__()
		self.__matrix_out__()
		
	def __sum_chetvert__(self):
		for i in range(len(self.arr)):
			for j in range(len(self.arr)):
				if i < j and i + j + 1 < len(self.arr):
					self.my_dict['Верхняя четверть'] += self.arr[i][j]
				if i < j and i + j + 1 > len(self.arr):
					self.my_dict['Правая четверть'] += self.arr[i][j]
				if i > j and i + j + 1 > len(self.arr):
					self.my_dict['Нижняя четверть'] += self.arr[i][j]
				if i > j and i + j + 1 < len(self.arr):
					self.my_dict['Левая четверть'] += self.arr[i][j]
					
	def __matrix_out__(self):
		for k, v in self.my_dict.items():
			print(f'{k}: {v}')
		
if __name__ == '__main__':
	Matrix(int(input()))