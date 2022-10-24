class Convert:
	def __init__(self, s):
		self.s = s
		self.__convert__()
		
	def __convert__(self):
		if 5 == len(self.s):
			self.s = self.s[::-1]
		else:
			self.s = self.s[0] + self.s[-1:0:-1]
		print(int(self.s))
		
if __name__ == '__main__':
	Convert(input())