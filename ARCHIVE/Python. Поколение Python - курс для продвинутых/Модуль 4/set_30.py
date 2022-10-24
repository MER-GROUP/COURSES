class MySet:
	def __init__(self, arr):
		inter = set(arr[0]).intersection(*arr)
		union = set(arr[0]).union(*arr)
		print(*sorted(union - inter))
		
if __name__ == '__main__':
	MySet([list(map(int, input().split())) for _ in range(3)])