class Matrix:
	def __init__(self, n):
		self.arr = [input().split() for _ in range(n)]
		self.__matrix_yes_no()
		
	def __is_matrix_sim__(self):
		for i in range(len(self.arr)):
			#for j in range(len(self.arr)):
			for j in range(i + 1):
				if not self.arr[i][j] == self.arr[j][i]:
					return False
		else: return True
		
	def __matrix_yes_no(self):
		if self.__is_matrix_sim__():
			print('YES')
		else: print('NO')
		
if __name__ == '__main__':
	Matrix(int(input()))