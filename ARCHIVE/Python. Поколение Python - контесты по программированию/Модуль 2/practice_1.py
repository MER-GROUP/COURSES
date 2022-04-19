class Algo:
	def __init__(self, n):
		self.__algo(n)
		
	def __algo(self, n):
		s = ''
		c = ''
		for i in range(1, n + 1):
			s += str(i) * i
			if n < len(s):
				if 1 == n % 2:
					c += str(i)
				break
			c += f'{i}' * i
		print(' '.join(c))
			
		
if __name__ == '__main__':
	Algo(int(input()))