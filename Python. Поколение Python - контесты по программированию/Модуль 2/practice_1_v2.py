class Seq:
	def __init__(self, n):
		self.__algo3(n)
		
	def __algo3(self, n):
		res = list()
		check = False
		for i in range(1, n + 1):
			for _ in range(i):
				res.append(str(i))
				if n == len(res):
					check = True
					break
			if check:
				break
		# print(' '.join(res))
		print(*res)
		
	def __algo2(self, n):
		res = list()
		for i in range(1, n + 1):
			for _ in range(i):
				res.append(str(i))
		print(' '.join(res[: n]))
		
	def __algo1(self, n):
		res = str()
		i = int(1)
		while len(res) < n:
			res += str(i) * i
			i += 1
		print(' '.join(res[: n]))
		
if __name__ == '__main__':
	Seq(int(input()))