from fractions import Fraction as F
from math import factorial

class Drob:
	def __init__(self, n):
		print(self.__alg(n))
		
	def __alg(self, n):
		return sum(F(1, factorial(i)) for i in range(1, n+1))
		
if __name__ == '__main__':
	Drob(int(input()))