class Matrix:
	def __init__(self, n):
		self.arr = [input().split() for _ in range(n)]
		self.matrix_rev_diag()
		self.matrix_out()
		
	def matrix_rev_diag(self):
		for i in range(len(self.arr)):
			self.arr[i][i], self.arr[len(self.arr) - i - 1][i] = self.arr[len(self.arr) - i - 1][i], self.arr[i][i]
			
	def matrix_out(self):
		for i in self.arr:
			print(*i)
		
if __name__ == '__main__':
	Matrix(int(input()))