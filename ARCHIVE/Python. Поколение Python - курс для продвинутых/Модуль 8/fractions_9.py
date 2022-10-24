from fractions import Fraction as F

class Union:
	def __init__(self, n):
		half_less = (n / 2) - 1 if 0 == n % 2 else n // 2
		half_less = int(half_less)
		print(self.__algo(half_less, n))
		
	def __algo(self, half_less, n):
		a = half_less
		b = n - a
		res = F(a, b)
		while True:
			if a == res.numerator and b == res.denominator:
				return res
			a -= 1
			b = n - a
			res = F(a, b)
		
if __name__ == '__main__':
	Union(int(input()))