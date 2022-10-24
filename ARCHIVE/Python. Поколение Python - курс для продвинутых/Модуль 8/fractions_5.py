from fractions import Fraction

class Drob:
	def __init__(self, a, b):
		print(Fraction(a, b))
		
if __name__ == '__main__':
	Drob(int(input()), int(input()))