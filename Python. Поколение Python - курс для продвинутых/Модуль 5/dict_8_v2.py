class MyDict:
	def __init__(self, n):
		self.digit = dict(zip('0123456789', 'zero one two three four five six seven eight nine'.split()))
		self.__convert(n)
					
	def __convert(self, n):
		for i in n:
			print(self.digit[i], end=' ')
		
		
if __name__ == '__main__':
	MyDict(input())