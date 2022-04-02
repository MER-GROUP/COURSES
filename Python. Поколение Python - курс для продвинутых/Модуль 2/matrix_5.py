class Matrix:
	def matrix_in(self, n):
		arr = [list(map(int, input().split())) for _ in range(n)]
		return arr
		
	def matrix_sled(self, arr):
		sm = int()
		for i in range(len(arr)):
			sm += arr[i][i]
		return sm
		
if __name__ == '__main__':
	m = Matrix()
	arr = m.matrix_in(int(input()))
	# print(arr)
	print(m.matrix_sled(arr))