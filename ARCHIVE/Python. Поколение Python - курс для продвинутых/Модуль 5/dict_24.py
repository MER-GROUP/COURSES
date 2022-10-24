class Sinonim:
	def __init__(self, n):
		dictor = dict()
		for i in range(n):
			arr = input().split()
			dictor[arr[0].strip()] = arr[1: ]
		find = [input().strip() for _ in range(int(input()))]
		print(*self.__search(find, dictor), sep='\n')
		
	def __search(self, find, dictor):
		arr = list()
		for i in find:
			check = False
			for k, v in dictor.items():
				for city in v:
					if i == city:
						arr.append(k)
						check = True
						break
				if check:
					break
		return arr
		
if __name__ == '__main__':
	Sinonim(int(input()))