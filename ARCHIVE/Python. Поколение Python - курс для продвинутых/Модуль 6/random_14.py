from string import ascii_letters, digits, ascii_lowercase, ascii_uppercase
from random import sample, shuffle

class GenPass:
	symbols = (ascii_letters + digits).replace('l', '').replace('I', '').replace('1', '').replace('o', '').replace('O', '').replace('0', '')
	letters_lower = ascii_lowercase.replace('l', '').replace('o', '')
	letters_upper = ascii_uppercase.replace('I', '').replace('O', '')
	digits_filter = digits.replace('0', '').replace('1', '')
	
	def __init__(self, n, m):
		for i in self.generate_passwords(n, m):
			print(''.join(i))
		
	def generate_password(self, length):
		start = sample(self.letters_lower, 1) + sample(self.letters_upper, 1) + sample(self.digits_filter, 1)
		end = sample(self.symbols, length - len(start))
		res = start + end
		shuffle(res)
		return res
		
		
	def generate_passwords(self, count, length):
		res = [self.generate_password(length) for _ in range(count)]
		return res
		
if __name__ == '__main__':
	GenPass(int(input()), int(input()))