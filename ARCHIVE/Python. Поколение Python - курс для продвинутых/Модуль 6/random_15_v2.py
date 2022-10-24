from string import digits, ascii_lowercase, ascii_uppercase
from random import choice, shuffle

class GenPass:
	letters_lower = [i for i in ascii_lowercase if not 'ol' == i]
	letters_upper = [i for i in ascii_uppercase if not 'IO' == i]
	digits_filter = list(digits[2 :])
	symbols = letters_lower + letters_upper + digits_filter
	
	def __init__(self, n, m):
		print(*self.generate_passwords(n, m), sep='\n')
		
	def generate_password(self, length):
		res = [choice(i) for i in (self.digits_filter, self.letters_lower, self.letters_upper)] + [choice(self.symbols) for _ in range(3, length)]
		shuffle(res)
		return ''.join(res)
		
		
	def generate_passwords(self, count, length):
		res = [self.generate_password(length) for _ in range(count)]
		return res
		
if __name__ == '__main__':
	GenPass(int(input()), int(input()))