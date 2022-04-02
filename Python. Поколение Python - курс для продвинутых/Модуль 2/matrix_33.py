class Matrix:
	def __init__(self, s, n):
		self.arr = s.split()
		self.n = int(n)
		self.res = [list() for i in range(int(n))]
		self.__matrix_alg__()
		
	def __matrix_alg__(self):
		cnt = int()
		for i in self.arr:
			self.res[cnt].append(i)
			cnt += 1
			if self.n == cnt:
				cnt = int()
		print(self.res)
		
if __name__ == '__main__':
	Matrix(input(), input())