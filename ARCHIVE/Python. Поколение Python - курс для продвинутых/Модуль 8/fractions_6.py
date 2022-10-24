from fractions import Fraction as F

class Drob:
	def __init__(self, d1, d2):
		print(f'{d1} + {d2} = {F(d1) + F(d2)}')
		print(f'{d1} - {d2} = {F(d1) - F(d2)}')
		print(f'{d1} * {d2} = {F(d1) * F(d2)}')
		print(f'{d1} / {d2} = {F(d1) / F(d2)}')
		
if __name__ == '__main__':
	Drob(input(), input())