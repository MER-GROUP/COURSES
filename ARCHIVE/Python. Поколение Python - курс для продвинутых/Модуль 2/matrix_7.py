class Matrix:
	def __init__(self, n=0):
		self.arr = [list(map(int, input().split())) for _ in range(n)]
		print(self.__max_el_main_diag_less__())
		
	def __max_el_main_diag_less__(self):
		el = list()
		for i in range(len(self.arr)):
			for j in range(len(self.arr)):
				if i >= j:
					el.append(self.arr[i][j])
		return max(el)
		
if __name__ == '__main__':
	Matrix(int(input()))