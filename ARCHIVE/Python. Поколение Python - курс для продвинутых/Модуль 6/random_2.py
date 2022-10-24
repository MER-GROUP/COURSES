from random import randint

class Orel:
	def __init__(self, n):
		self.orel = dict(zip([0, 1], ['Орел', 'Решка']))
		self.__orel(n)
		
	def __orel(self, n):
		for i in range(n):
			print(self.orel[randint(0, 1)])
		
if __name__ == '__main__':
	Orel(int(input()))