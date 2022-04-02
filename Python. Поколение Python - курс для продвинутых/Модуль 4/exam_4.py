class MySet:
	def __init__(self, arr):
		print(len(arr) - len(set(arr)))
		
if __name__ == '__main__':
	MySet(list(map(int, input().split())))