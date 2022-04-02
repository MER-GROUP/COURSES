from random import randrange

class Loto:
	def __init__(self):
		self.generate()
		
	def generate(self):
		loto = set()
		while 100 > len(loto):
			s = ''.join([str(randrange(10)) for _ in range(7)])
			if '0' == s[0]:
				continue
			else:
				loto.add(int(s))
		print(*loto, sep='\n')
		
if __name__ == '__main__':
	Loto()