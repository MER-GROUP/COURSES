class Mobile:
	def __init__(self,n):
		dictor = dict()
		for _ in range(n):
			v, k = input().lower().split()
			dictor.setdefault(k, []).append(v)
		find = [input().lower().strip() for _ in range(int(input()))]
		self.__search(find, dictor)
		
	def __search(self, find, dictor):
		for i in find:
			print(*dictor.get(i, ['абонент не найден']))
		
		
if __name__ == '__main__':
	Mobile(int(input()))