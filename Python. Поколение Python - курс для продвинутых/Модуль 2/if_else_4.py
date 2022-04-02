class Digit:
	def __init__(self, arr):
		# print(arr.insert.__doc__)
		arr.insert(0, arr.pop())
		print(*arr)
		
if __name__ == '__main__':
	Digit(list(map(int, input().split())))