class MySet:
	def __init__(self, n):
		for _ in range(n):
			print(len(set(input().lower())))
		
if __name__ == '__main__':
	MySet(int(input()))