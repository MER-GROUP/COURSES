class Sinonim:
	def __init__(self, n):
		dictor = dict()
		for _ in range(n):
			k, v = input().split()
			dictor[k.strip()] = v.strip()
			dictor[v.strip()] = k.strip()
		find = input().strip()
		print(self.__sinonim(find, dictor))
		
	def __sinonim(self, find, dictor):
		return dictor[find]
		
if __name__ == '__main__':
	Sinonim(int(input()))