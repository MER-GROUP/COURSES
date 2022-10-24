class MySet:
	def __init__(self, n):
		arr = [input() for _ in range(n)]
		print(*sorted(set(arr[0]).intersection(*arr[1 : ])))
		
if __name__ == '__main__':
	MySet(int(input()))