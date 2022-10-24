class MySet:
	def __init__(self, n):
		s = str()
		for _ in range(n):
			s += input().lower()
		print(len(set(s)))
		
if __name__ == '__main__':
	MySet(int(input()))