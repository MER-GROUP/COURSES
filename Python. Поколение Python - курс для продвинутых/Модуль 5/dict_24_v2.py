class Sinonim:
	def __init__(self, n):
		dictor = dict()
		for i in range(n):
			k, *v = input().split()
			dictor.update(dict.fromkeys(v, k))
		find = [input().split() for _ in range(int(input()))]
		self.__search(find, dictor)
		print(*self.__search(find, dictor), sep='\n')
		
	def __search(self, find, dictor):
		arr = [dictor[str(*i)] for i in find]
		return arr
		
if __name__ == '__main__':
	Sinonim(int(input()))