class MyDict:
	def __init__(self, arr):
		dictor = dict()
		self.__fix(dictor, arr)
		
	def __fix(self, dictor, arr):
		for i in arr:
			if i not in dictor:
				dictor[i] = 0
			else:
				dictor[i] += 1
				k = i + '_' + str(dictor[i])
				dictor[k] = 0
		print(*list(dictor.keys()))
		
if __name__ == '__main__':
	MyDict(input().split())