class Matrix:
	def __init__(self, n=0, m=0):
		self.arr = [list(map(int, input().split())) for _ in range(n)]
		self.idx = [0, 0]
		self.__matrix_max_el_idx__()
		print(self.idx[0], self.idx[1])
		
	def __matrix_max_el_idx__(self):
		for i in range(len(self.arr)):
			for j in range(len(self.arr[0])):
				if self.arr[self.idx[0]][self.idx[1]] < self.arr[i][j]:
					self.idx[0] = i
					self.idx[1] = j
		
if __name__ == '__main__':
	Matrix(int(input()), int(input()))