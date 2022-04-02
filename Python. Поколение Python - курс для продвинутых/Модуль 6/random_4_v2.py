from random import randint

class PSWD:
	def __init__(self, n):
		print(self.__pswd_gen(n))
		
	def __pswd_gen(self, n):
		abc = str()
		for c in range(n):
			abc += [chr(randint(65, 90)), chr(randint(97, 122))][randint(0, 1)]
		return abc
		
if __name__ == '__main__':
	PSWD(int(input()))