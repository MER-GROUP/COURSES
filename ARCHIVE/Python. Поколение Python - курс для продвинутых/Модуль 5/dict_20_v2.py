class MyDict:
	def __init__(self, n):
		dictor = dict()
		for _ in range(n):
			k, v = input().split(': ')
			dictor[k.lower()] = v.strip()
		# print(dictor)
		m = int(input())
		find = [input().strip().lower() for _ in range(m)]
		# print(find)
		self.__find(dictor, find)
		
	def __find(self, dictor, find):
		for word in find:
			print(dictor.get(word, 'Не найдено'))
		
if __name__ == '__main__':
	MyDict(int(input()))