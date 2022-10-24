class Sinonim:
	def __init__(self, n):
		dictor = dict()
		for _ in range(n):
			k, v = input().split()
			dictor[k.strip()] = v.strip()
		find = input().strip()
		print(self.__sinonim(find, dictor))
		
	def __sinonim(self, find, dictor):
		if find in dictor:
			return dictor[find]
		else:
			for k, v in dictor.items():
				if v == find:
					return k
		
if __name__ == '__main__':
	Sinonim(int(input()))