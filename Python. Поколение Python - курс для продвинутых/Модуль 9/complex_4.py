class Compl:
	def __init__(self, n, z1, z2):
		print(self.__pow(z1, n) + self.__pow(z2, n) + self.__pow(z1.conjugate(), n) + self.__pow(z2.conjugate(), n + 1))
	
	def __pow(self, z, n):
		res = z
		for i in range(n - 1):
			res *= z
		return res
		
if __name__ == '__main__':
	Compl(int(input()), complex(input()), complex(input()))