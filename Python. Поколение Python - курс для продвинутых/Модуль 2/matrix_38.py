class Matrix:
	def __init__(self, n):
		self.arr = [list(map(int, input().split())) for i in range(n)]
		self.__matrix_alg__()
		
	def __matrix_alg__(self):
		check = sum(range(1, len(self.arr) + 1))
		for i in range(len(self.arr)):
			if not sum(self.arr[i]) == check:
				print('NO')
				break
			sm = int()
			for j in range(len(self.arr)):
				sm += self.arr[j][i]
			if not sm == check:
				print('NO')
				break
		else:
			print('YES')
		
if __name__ == '__main__':
	Matrix(int(input()))