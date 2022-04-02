class Algo:
	def __init__(self, s1, s2):
		self.__algo(s1, s2)
		
	def __algo(self, s1, s2):
		c1 = sorted(s1)
		c2 = sorted(s2)
		for i, j in zip(c1, c2):
			if i != j:
				print(j)
				break
		else:
			print(c2[-1])
			
		
if __name__ == '__main__':
	Algo(input(), input())