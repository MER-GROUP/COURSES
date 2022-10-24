from string import ascii_letters, digits
from random import sample

class GenPass:
	symbols = ''.join(set(ascii_letters) | set(digits) - set('lI1oO0'))
	
	def __init__(self, n, m):
		print(*self.generate_passwords(n, m), sep='\n')
		
	def generate_password(self, length):
		return ''.join(sample(self.symbols, length))
		
		
	def generate_passwords(self, count, length):
		res = [self.generate_password(length) for _ in range(count)]
		return res
		
if __name__ == '__main__':
	GenPass(int(input()), int(input()))