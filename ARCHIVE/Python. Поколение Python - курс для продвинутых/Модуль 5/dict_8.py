class MyDict:
	def __init__(self, n):
		self.digit = {'0': 'zero',
							'1': 'one',
							'2': 'two',
							'3': 'three',
							'4': 'four',
							'5': 'five',
							'6': 'six',
							'7': 'seven',
							'8': 'eight',
							'9': 'nine'}
		self.__convert(n)
					
	def __convert(self, n):
		for i in range(len(n)):
			print(self.digit[n[i]], end=' ')
		
		
if __name__ == '__main__':
	MyDict(input())