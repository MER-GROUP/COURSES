class Matrix:
	def __init__(self, n=0):
		self.arr = [list(map(int, input().split())) for _ in range(n)]
		print(self.__max_el_main_diag_less__())
		
	def __max_el_main_diag_less__(self):
		el = self.arr[0][0]
		for i in range(len(self.arr)):
			for j in range(len(self.arr)):
				if el < self.arr[i][j] and ((i >= j and i + j + 1 <= len(self.arr)) or (i <= j and i + j + 1 >= len(self.arr))):
					el = self.arr[i][j]
		return el
		
if __name__ == '__main__':
	Matrix(int(input()))