class Algo:
	def __init__(self, s):
		self.__algo(s)
		
	def __algo(self, s):
		i = 0
		res = ''
		while i < len(s):
			# print(s[i], end='')
			if '_' == s[i]:
				res += '0'
			elif '|' == s[i]:
				res += '1'
				i += 1
			else:
				res += '0'
			i += 1
		print(res)
		
if __name__ == '__main__':
	Algo(input())