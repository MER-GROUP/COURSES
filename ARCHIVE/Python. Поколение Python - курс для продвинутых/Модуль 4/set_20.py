class MySet:
	def __init__(self, arr):
		for i in range(len(arr)):
			if 0 == i:
				print('NO')
			elif arr[i] in arr[: i]:
				print('YES')
			else:
				print('NO')
		
if __name__ == '__main__':
	MySet(list(map(int, input().split())))