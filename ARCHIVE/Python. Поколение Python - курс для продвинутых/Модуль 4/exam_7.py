class MySet:
	def __init__(self):
		one = {*map(int, input().split())}
		two = {*map(int, input().split())}
		if not one.intersection(two):
			print('BAD DAY')
		else:
			arr = sorted(one.intersection(two), reverse=True)
			print(*arr)
		
if __name__ == '__main__':
	MySet()