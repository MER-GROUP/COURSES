class MySet:
	def __init__(self, arr1, arr2):
		print(*sorted(set(arr1).intersection(arr2)))
		
if __name__ == '__main__':
	MySet(*[list(map(int, input().split())) for _ in range(2)])