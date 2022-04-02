class Matrix:
	def __init__(self, n, m):
		self.arr = [[0] * m for i in range(n)]
		self.it = iter(range(1, (n * m) + 1))
		self.__matrix_alg__(n, m, self.it)
		self.__matrix_print__()
		
	def __matrix_print__(self):
		for i in self.arr:
			for j in i:
				print(str(j).ljust(3), end=' ')
			print()
			
	def __matrix_alg__(self, n, m, it):
		i, j, = [int()] * 2
		# cnt = int()
		right = True
		down = True
		left = True
		up = True
		
		while True:
			if right and j < m and 0 == self.arr[i][j]:
				self.arr[i][j] = next(it)
				j += 1
				continue
			else:
				if right:
					j -= 1
					i += 1
					right = False
					down = True
			
			if down and i < n and 0 == self.arr[i][j]:
				self.arr[i][j] = next(it)
				i += 1
				continue
			else:
				if down:
					i -= 1
					j -= 1
					down = False
					left = True
					
			if left and 0 <= j and 0 == self.arr[i][j]:
				self.arr[i][j] = next(it)
				j -= 1
				continue
			else:
				if left:
					j += 1
					i -= 1
					left = False
					up = True
					
			#print(f'i = {i}, j = {j}')	
			
			if up and 0 <= i and 0 == self.arr[i][j]:
				self.arr[i][j] = next(it)
				i -= 1
				continue
			else:
				if up:
					i += 1
					j += 1
					up = False
					right = True
				
			# cnt += 1
			# if 1000 == cnt:
				# break
			if i == n or j == m or not 0 == self.arr[i][j]:
				break
		
if __name__ == '__main__':
	Matrix(*list(map(int, input().split())))