class Discrim:
	def __init__(self, a, b, c):
		print(self.__alg__(a, b, c))
		
	def __alg__(self, a, b, c):
		x1 = -b / (2 * a)
		x2 = (4 * a * c - b ** 2) / (4 * a)
		return x1, x2
		
if __name__ == '__main__':
	Discrim(*[int(input()) for _ in range(3)])