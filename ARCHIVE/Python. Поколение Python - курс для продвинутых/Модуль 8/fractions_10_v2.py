from fractions import Fraction as F

class Union:
	def __init__(self, n):
		print(*self.__algo(n), sep='\n')
		
	def __algo(self, n):
		arr = set()
		for i in range(1, n + 1):
			for j in range(i + 1, n + 1):
				arr.add(F(i, j))
		return sorted(arr)
		
if __name__ == '__main__':
	Union(int(input()))