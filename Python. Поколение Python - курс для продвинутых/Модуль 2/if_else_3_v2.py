class Digit:
	def __init__(self, arr):
		for i in range(1, len(arr), 2):
				arr[i - 1], arr[i] = arr[i], arr[i - 1]
		print(*arr)
		
if __name__ == '__main__':
	Digit(input().strip().split())