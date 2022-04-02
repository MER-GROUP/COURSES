class Digit:
	def __init__(self, arr):
		print(*[arr[-1]] + arr[:-1])
		
if __name__ == '__main__':
	Digit(list(map(int, input().split())))