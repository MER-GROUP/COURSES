class Flaviy:
	def __init__(self, n, k):
		self.n = n
		self.k = k
		self.__flaviy__()
		
	def __flaviy__(self):
		arr = [i for i in range(1, self.n + 1)]
		while True:
			tmp = list()
			i = int()
			if self.k <= len(arr) and 1 != len(arr):
				tmp = arr[:self.k - 1]
				arr.extend(tmp)
				del arr[:self.k]
			elif 1 == len(arr):
				break
			else:
				for k in range(self.k):
					i += 1
					if i > len(arr):
						i = 1
				i = i - 1
				if 0 == i:
					del arr[i]
				else:
					tmp = arr[:i]
					arr.extend(tmp)
					del arr[:i + 1]
		print(*arr)

n, k = (int(input()) for _ in range(2))
Flaviy(n, k)