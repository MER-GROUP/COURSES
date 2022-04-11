class Algo:
	def __init__(self, s):
		self.__algo3(s)
		
	def __algo(self, s):
		list1 = s
		list1 = list1.replace('|¯', '1')
		list1 = list1.replace('|_', '1')
		list1 = list1.replace('¯', '0')
		list1 = list1.replace('_', '0')
		print(list1)

	def __algo2(self, s):
		str_code = s
		i = 0
		result = ''
		while i < len(str_code):
			c = int(str_code[i] == '|')
			result += str(c)
			i += 1 + c
		print(result)

	def __algo3(self, w):
		s = w
		for i in range(len(s)):
			if s[i] == '|':
				continue
			if s[i-1] == '|':
				print('1', end='')
			else:
				print('0', end='')
		
if __name__ == '__main__':
	Algo(input())