class MySet:
	def __init__(self, arr):
		# inter = set(arr[0]).intersection(arr[1])
		# print(*sorted(inter.difference(arr[2]), reverse=True))
		print(*sorted(set(arr[0]) & set(arr[1]) - set(arr[2]), reverse=True))
		
if __name__ == '__main__':
	MySet([list(map(int, input().split())) for _ in range(3)])