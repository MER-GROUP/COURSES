class MySet:
	def __init__(self, arr):
		print(*sorted(set(arr[2]).difference(*arr[: -1]), reverse=True))
		
if __name__ == '__main__':
	MySet([list(map(int, input().split())) for _ in range(3)])