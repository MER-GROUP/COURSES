class Nomer:
	def __init__(self, arr):
		self.dictor = dict()
		self.__nomer(arr)
		
	def __nomer(self, arr):
		for i in arr:
			self.dictor[i] = self.dictor.get(i, 0) + 1
			print(self.dictor[i], end=' ')
		
if __name__ == '__main__':
	Nomer(input().split())