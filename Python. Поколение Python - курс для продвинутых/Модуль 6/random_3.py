from random import randrange

class Kubik:
	def __init__(self, n):
		self.__gran(n)
		
	def __gran(self, n):
		for i in range(n):
			print(randrange(1, 7))
		
if __name__ == '__main__':
	Kubik(int(input()))