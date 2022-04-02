from string import ascii_lowercase

class Algo:
	def __init__(self, s):
		print(self.__algo(s))
		
	def __algo(self, s):
		arr = [i for i in s if i in ascii_lowercase]
		for i in range(len(arr)):
			tmp = arr.copy()
			del tmp[i]
			if tmp == tmp[: : -1]:
				return True
		return False
		
		
if __name__ == '__main__':
	Algo(input())