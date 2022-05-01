from string import ascii_lowercase

class Algo:
	def __init__(self, s):
		print(self.__algo(s))
		
	def __algo(self, s):
		res = [i for i in s if i in ascii_lowercase]
		s = ''
		for i in range(len(res)):
			for j in range(len(res)):
				if i != j:
					s += res[j]
			if s == s[::-1]:
				return True
			s = ''
		return False
		
		
if __name__ == '__main__':
	Algo(input())