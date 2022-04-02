from random import sample

class Loto:
	def __init__(self):
		self.generate()
		
	def generate(self):
		print(*sample(range(int(1e6), int(1e7)), 100), sep='\n')
		
if __name__ == '__main__':
	Loto()