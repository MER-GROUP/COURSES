class MyDict:
	def __init__(self, n):
		dictor = dict()
		for _ in range(n):
			arr = input().split(':')
			dictor[arr[0].lower()] = arr[1].strip()
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