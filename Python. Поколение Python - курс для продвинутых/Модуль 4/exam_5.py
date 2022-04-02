class MySet:
	def __init__(self, n):
		arr = [input() for _ in range(n)]
		end = input()
		print(['REPEAT', 'OK'][set(arr).isdisjoint({end})])
		
if __name__ == '__main__':
	MySet(int(input()))