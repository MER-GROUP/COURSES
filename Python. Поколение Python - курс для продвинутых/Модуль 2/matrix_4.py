class Matrix:
	def __init__(self):
		pass

	def matrix_in(self, rows, cols):
		arr = [[input() for _ in range(cols)] for _ in range(rows)]
		return arr
		
	def matrix_out(self, arr):
		for i in arr:
			for j in i:
				print(j, end=' ')
			print()
			
	def matrix_out_reverse_rows_cols(self, arr):
		for j in range(len(arr[0])):
			for i in range(len(arr)):
				print(arr[i][j], end=' ')
			print()
		
if __name__ == '__main__':
	m = Matrix()
	arr = m.matrix_in(int(input()), int(input()))
	m.matrix_out(arr)
	print()
	m.matrix_out_reverse_rows_cols(arr)