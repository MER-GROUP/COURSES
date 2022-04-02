class MySet:
	def __init__(self, arr):
		my_set = set(range(11))
		union = set(arr[0]).union(*arr[1:])
		print(*sorted(my_set - union))
		
if __name__ == '__main__':
	MySet([list(map(int, input().split())) for _ in range(3)])