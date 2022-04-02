class Matrix:
	def __init__(self, n=0, m=0):
		self.arr = [list(map(int, input().split())) for _ in range(n)]
		
	def matrix_print(self):
		for i in self.arr:
			print(*i)
			
	def matrix_mult(self, arr1, arr2):
		arr = [[0] * len(arr2[0]) for _ in range(len(arr1))]
		for i in range(len(arr1)):
			for j in range(len(arr2[0])):
				for q in range(len(arr2)):
					arr[i][j] += arr1[i][q] * arr2[q][j]
		self.arr = arr
		
if __name__ == '__main__':
	a = Matrix(*list(map(int, input().split())))
	input()
	b = Matrix(*list(map(int, input().split())))
	c = Matrix()
	c.matrix_mult(a.arr, b.arr)
	c.matrix_print()