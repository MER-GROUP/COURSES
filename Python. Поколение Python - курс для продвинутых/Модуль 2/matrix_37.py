class Matrix:
	def __init__(self, n):
		self.arr = [list(map(int, input().split())) for i in range(n)]
		self.__matrix_alg__()
		
	def __matrix_alg__(self):
		diag_down = list()
		diag_up = list()
		check = False
		for k in range(len(self.arr)):
			for i in range(len(self.arr)):
				for j in range(len(self.arr)):
					if i - k == j:
						diag_down.append(self.arr[i][j])
					if i + k == j:
						diag_up.append(self.arr[i][j])
			for dd in range(len(diag_down)):
				if not diag_down[dd] == diag_down[~dd]:
					print('NO')
					check = True
					break
				if not diag_up[dd] == diag_up[~dd]:
					print('NO')
					check = True
					break
			diag_down.clear()
			diag_up.clear()
			if check:
				break
		else:
			print('YES')
		
if __name__ == '__main__':
	Matrix(int(input()))