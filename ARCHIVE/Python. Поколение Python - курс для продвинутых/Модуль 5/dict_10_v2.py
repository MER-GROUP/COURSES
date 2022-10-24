class Mobile:
	def __init__(self, s):
		self.touch = dict(zip('1 2 3 4 5 6 7 8 9'.split(), '.,?!: ABC DEF GHI JKL MNO PQRS TUV WXYZ'.split()))
		self.touch['0'] = ' '
		self.__crypt(s)
		
	def __crypt(self, s):
		for c in s:
			for k, v in self.touch.items():
				if c in v:
					print(k * (v.index(c) + 1), end='')
					break
		
if __name__ == '__main__':
	Mobile(input().upper())