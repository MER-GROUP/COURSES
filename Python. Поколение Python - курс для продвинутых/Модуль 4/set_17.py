class MySet:
	def __init__(self, n):
		arr = [input().lower() for _ in range(n)]
		for i in arr:
			print(len(set(i)))
		
if __name__ == '__main__':
	MySet(int(input()))