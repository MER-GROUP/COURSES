class Matrix:
	def __init__(self):
		pass
		
	@staticmethod
	def arr_init():
		n = int(input())
		return [[0 for _ in range(n)] for _ in range(n)]
		
	@staticmethod
	def arr_out(arr):
		for i in arr:
			for j in i:
				#print(f'{j : 2d}', end=' ')
				#print(j, end='\t')
				print(j, end=' ')
			print()
			
	@staticmethod
	def arr_tire():
		print('--------------------')
			
	@staticmethod
	def arr_spiral(arr):
		i, j, step = [0] * 3
		el = 1
		while True:
			#right
			while j < len(arr[0]):
				if 0 == arr[i][j]:
					arr[i][j] = el
					el += 1
				else: break
				j += 1
			j -= 1
			#down
			while i < len(arr):
				i += 1
				if i == len(arr):
					break
				elif 0 == arr[i][j]:
					arr[i][j] = el
					el += 1
				else: break
			i -= 1
			#left
			while 0 <= j:
				j -= 1
				if 0 == arr[i][j]:
					arr[i][j] = el
					el += 1
				else: break
			j += 1
			#up
			while 0 < i:
				i -= 1
				if 0 == arr[i][j]:
					arr[i][j] = el
					el += 1
				else: break
			#spiral
			if step <= len(arr) // 2 + 1:
				i, j = [step] * 2
				step += 1
			else:
				break
			
		
def main():
	arr = Matrix.arr_init()
	#Matrix.arr_out(arr)
	#Matrix.arr_tire()
	Matrix.arr_spiral(arr)
	Matrix.arr_out(arr)
	
if __name__ == '__main__':
	main()