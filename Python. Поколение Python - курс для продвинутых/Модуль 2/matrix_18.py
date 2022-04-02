class Matrix:
	def __init__(self, n):
		self.arr = [list(map(int, input().split())) for _ in range(n)]
		self.__matrix_out__()
		
	def __matrix_out__(self):
		if self.__is_matrix_magic__():
			print('YES')
		else:
			print('NO')
			
	def __is_matrix_magic__(self):
		rows_sum = list()
		cols_sum = list()
		main_diag = int()
		no_main_diag = int()
		arr = list()
		
		for i in self.arr:
			rows_sum.append(sum(i))
			if 1 == len(set(i)):
				return False
			
		for j in range(len(self.arr)):
			tmp = list()
			for i in range(len(self.arr)):
				tmp.append(self.arr[i][j])
			if 1 == len(set(tmp)):
				return False
			cols_sum.append(sum(tmp))
			
		for i in range(len(self.arr)):
			main_diag += self.arr[i][i]
			no_main_diag += self.arr[len(self.arr) - i - 1][len(self.arr) - i - 1]
			
		arr += rows_sum + cols_sum + [main_diag] + [no_main_diag]
		#print(arr)
		
		for i in range(1, len(arr)):
			if not arr[i - 1] == arr[i] or 14 > arr[i - 1] or 14 > arr[i]:
				return False
		else:
			return True
		
if __name__ == '__main__':
	Matrix(int(input()))