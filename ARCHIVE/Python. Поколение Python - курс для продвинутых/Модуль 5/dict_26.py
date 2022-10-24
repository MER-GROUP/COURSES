class Analis:
	def __init__(self, s, n):
		abc = dict()
		for _ in range(n):
			v, k = input().split(': ')
			abc[int(k)] = v
		self.__deshifr(s, abc)
			
	def __deshifr(self, s, abc):
		for i in s:
			print(abc[s.count(i)], end='')
		
if __name__ == '__main__':
	Analis(input(), int(input()))