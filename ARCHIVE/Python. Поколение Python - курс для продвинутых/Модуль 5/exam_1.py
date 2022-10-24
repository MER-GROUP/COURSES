class DNK:
	def __init__(self, s):
		self.shifr = {'T': 'A', 'G': 'C', 'C': 'G', 'A': 'U'}
		self.__dnk_to_rnk(s)
		
	def __dnk_to_rnk(self, s):
		for i in s:
			print(self.shifr[i], end='')
		
if __name__ == '__main__':
	DNK(input())