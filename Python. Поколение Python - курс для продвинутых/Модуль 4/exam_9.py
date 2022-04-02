class MySet:
	def __init__(self, m, n):
		mat = [input() for _ in range(m)]
		inf = [input() for _ in range(n)]
		print(len(set(mat).difference(inf)))
		
if __name__ == '__main__':
	MySet(int(input()), int(input()))