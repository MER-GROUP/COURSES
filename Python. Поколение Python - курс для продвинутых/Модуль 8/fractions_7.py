from fractions import Fraction as F

class Drob:
	def __init__(self, n):
		print(self.__alg(n))
		
	def __alg(self, n):
		res = F()
		for i in range(1,n + 1):
			res += F(f'1/{i**2}')
		return res
		
if __name__ == '__main__':
	Drob(int(input()))