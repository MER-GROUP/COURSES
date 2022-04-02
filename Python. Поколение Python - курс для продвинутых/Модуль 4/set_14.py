class MySet:
	def __init__(self, arr):
		print(('NO', 'YES')[set(arr[0]) == set(arr[1]) == set(arr[2])])
	
if __name__ == '__main__':
	MySet(input().split())