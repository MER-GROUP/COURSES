class Matrix:
	def __init__(self, n=0, m=0):
		self.arr = [list(map(int, input().split())) for _ in range(n)]
		
	def matrix_print(self):
		for i in self.arr:
			print(*i)
			
	def matrix_mult(self, arr1, arr2):
		arr = list()
		for i in range(len(arr1)):
			j = int()
			cnt = int()
			tmp = list()
			while True:
				for x in range(len(arr2[0])):
					sum = int()
					for y in range(len(arr2)):
						sum += arr1[i][j] * arr2[y][x]
						# print(f'i = {i}, j = {j}, y = {y}, x = {x}')
						# print(f'arr1[i][j] = {arr1[i][j]}, arr2[y][x] = {arr2[y][x]}')
						# print(f'sum = {sum}')
						j += 1
					if j >= len(arr1[0]):
						tmp.append(sum)
						j = int()
						cnt += 1
				if cnt >= len(arr1):
					arr.append(tmp)
					cnt = int()
					break
		self.arr = arr
		
if __name__ == '__main__':
	a = Matrix(*list(map(int, input().split())))
	input()
	b = Matrix(*list(map(int, input().split())))
	c = Matrix()
	c.matrix_mult(a.arr, b.arr)
	c.matrix_print()