class Matrix:
	def __init__(self, n):
		self.it = iter(range(2, n))
		self.arr = [[self.__matrix_in__(i, j, n) for j in range(n)] for i in range(n)]
		self.__matrix_out__()
		
	def __matrix_in__(self, i, j, n):
		if i == j or i == n - j - 1:
			return 1
		elif j > i and n > i + j + 1:
			if j < n // 2:
				return 2
			elif j > n // 2 and 1 == n % 2:
				return 3
			elif j >= n // 2 and 0 == n % 2:
				return 3
			else:
				return 0
		elif j < i and n < i + j + 1:
			if j < n // 2:
				return 2
			elif j > n // 2 and 1 == n % 2:
				return 3
			elif j >= n // 2 and 0 == n % 2:
				return 3
			else:
				return 0
		else:
			return 0
		
	def __matrix_out__(self):
		for i in self.arr:
			for j in i:
				print(j, end=' ')
			print()
		
if __name__ == '__main__':
	Matrix(int(input()))