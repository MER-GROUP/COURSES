from fractions import Fraction as F
from math import gcd

class Union:
	def __init__(self, n):
		a = n // 2
		b = n - a
		print(self.__algo(a, b))
		
	def __algo(self, a, b):
		while gcd(a, b) != 1:
			a -= 1
			b += 1
		return F(a, b)
		
if __name__ == '__main__':
	Union(int(input()))