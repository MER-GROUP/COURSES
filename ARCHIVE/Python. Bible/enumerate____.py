class Digit:
	def __init__(self):
		pass
	@staticmethod	
	def enter_line():
		return [int(i) for i in input().split()]
	@staticmethod
	def algo(arr, x):
		for ind, i in enumerate(arr):
			if x == i:
				print(ind, end=' ')
		else:
			if x not in arr:
				print('Отсутствует')
		
def main():
	arr = Digit.enter_line()
	x = int(input())
	Digit.algo(arr, x)
	
if __name__ == '__main__':
	main()