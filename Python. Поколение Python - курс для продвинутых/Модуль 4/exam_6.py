class MySet:
	def __init__(self, m, n):
		home = [input() for _ in range(m)]
		school = [input() for _ in range(n)]
		for i in range(n):
			print(['NO', 'YES'][school[i] in home])
		
if __name__ == '__main__':
	MySet(int(input()), int(input()))