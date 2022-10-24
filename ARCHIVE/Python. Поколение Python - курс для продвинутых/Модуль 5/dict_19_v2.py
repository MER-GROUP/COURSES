class MyDict:
	def __init__(self, arr):
		dictor = dict()
		self.__fix(dictor, arr)
		
	def __fix(self, dictor, arr):
		for i in arr:
			if i in dictor:
				print(f'{i}_{dictor[i]}', end=' ')
			else:
				print(i, end=' ')
			dictor[i] = dictor.get(i, 0) + 1
		
if __name__ == '__main__':
	MyDict(input().split())