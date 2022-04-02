from random import randrange

class PSWD:
	def __init__(self, n):
		# print(self.__abc_init())
		self.__pswd_gen(n, self.__abc_init())
		
	def __abc_init(self):
		little = list()
		big = list()
		for c in range(ord('a'), ord('z') + 1):
			little.append(chr(c))
		# print(little)
		for c in range(ord('A'), ord('Z') + 1):
			big.append(chr(c))
		# print(big)
		return little + big
		
	def __pswd_gen(self, n, arr):
		for i in range(n):
			print(arr[randrange(len(arr))], end='')
		
if __name__ == '__main__':
	PSWD(int(input()))