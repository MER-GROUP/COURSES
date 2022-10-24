class MySet:
	def __init__(self, n):
		# arr = [[int(i) for i in input()] for _ in range(n)]
		arr = [list(map(int, set(input()))) for _ in range(n)]
		# print(arr)
		tmp = set(arr[0])
		for i in range(1, n):
			tmp &= set(arr[i])
		print(*sorted(tmp))
		
if __name__ == '__main__':
	MySet(int(input()))