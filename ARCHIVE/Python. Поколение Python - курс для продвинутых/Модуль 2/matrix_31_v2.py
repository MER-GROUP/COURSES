import numpy as np

class Matrix:
	def __init__(self, n=0, m=0):
		self.arr = [list(map(int, input().split())) for _ in range(n)]
		
	def matrix_print(self):
		for i in self.arr:
			print(*i)
		
if __name__ == '__main__':
	a = Matrix(*list(map(int, input().split())))
	input()
	b = Matrix(*list(map(int, input().split())))
	a_np = np.matrix(a.arr)
	b_np = np.matrix(b.arr)
	c_np = a_np * b_np
	c = Matrix()
	c.arr = c_np.tolist()
	c.matrix_print()