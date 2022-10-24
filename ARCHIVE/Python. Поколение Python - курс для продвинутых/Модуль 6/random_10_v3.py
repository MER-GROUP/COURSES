class Loto:
	def __init__(self):
		self.generate()
		
	def generate(self):
		[print(i) for i in __import__('random').sample(range(int(1e6), int(1e7)), 100)]
		
if __name__ == '__main__':
	Loto()