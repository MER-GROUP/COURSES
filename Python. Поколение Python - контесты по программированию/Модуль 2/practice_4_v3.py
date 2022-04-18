# авторский алгоритм от BEEGIK
class Algo:
	def __init__(self, s):
		self.__algo(s)
		
	def __algo(self, s):
		code = s
		decode = ''
		counter = 0
		while counter < len(code):
			if code[counter] == '|':
				decode += '1'
				counter += 2
			else:
				decode += '0'
				counter += 1
		print(decode)
		
if __name__ == '__main__':
	Algo(input())