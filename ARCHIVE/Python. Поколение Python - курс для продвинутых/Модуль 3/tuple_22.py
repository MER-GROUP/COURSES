class School:
	def __init__(self, n):
		self.arrc = tuple([tuple(input().split()) for _ in range(n)])
		self.__print__(0)
		print()
		self.__print__(4)
		
	def __print__(self, mark=0):
		for i in self.arrc:
			if mark <= int(i[1]):
				print(*i)
		
if __name__ == '__main__':
	School(int(input()))