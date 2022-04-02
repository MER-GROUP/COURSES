class Digit:
	def __init__(self, s):
		self.s = s
		self.res = str()
		self.__usa_std__()
		
	def __usa_std__(self):
		if 3 < len(self.s):
			self.s = self.s[::-1]
			i = int()
			for j in range(len(self.s)):
				i += 1
				self.res += self.s[j]
				if 3 == i and j != len(self.s) - 1:
					i = 0
					self.res += ','
			self.res = self.res[::-1]
		else:
			self.res = self.s
		print(self.res)
		
if __name__ == '__main__':
	Digit(input())