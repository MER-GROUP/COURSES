class MyDict:
	def __init__(self, s):
		dictor = dict()
		for i in s:
			i = i.strip('.,!?:;-')
			dictor[i] = dictor.get(i, 0) + 1
		print(min(dictor, key=lambda x: (dictor[x], x)))
		
if __name__ == '__main__':
	MyDict(input().lower().split())