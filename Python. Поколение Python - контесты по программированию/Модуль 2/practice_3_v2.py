class Algo:
	def __init__(self, s1, s2):
		self.__algo(s1, s2)
		
	def __algo(self, s1, s2):
		a = s1
		b = s2
		for character in a:
			b = b.replace(character, '', 1)
		print(b)

	def __algo2(self, s1, s2):
		a = s1
		b = s2
		for i in set(b):
			if b.count(i) != a.count(i):
				print(i)
				break

	def __algo3(self, s1, s2):
		a = s1
		b = s2
		x = a + b
		for i in x:
			if x.count(i)%2 != 0:
				print(i)
				break
	
	def __algo4(self, s1, s2):
		from collections import Counter
		a, b = Counter(s1), Counter(s2)
		print(*list(b - a))

	def __algo5(self, s1, s2):
		a = list(s1)
		b = list(s2)
		for i in a:
			b.remove(i)
		print(*b)

	def __algo6(self, s1, s2):
		from collections import Counter
		string1, string2 = s1, s2
		print(next(iter(Counter(string2) - Counter(string1))))
			
		
if __name__ == '__main__':
	Algo(input(), input())