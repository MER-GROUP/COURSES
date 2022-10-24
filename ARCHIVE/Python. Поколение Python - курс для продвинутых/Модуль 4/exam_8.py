class MySet:
	def __init__(self):
		one = {*map(int, input().split())}
		two = {*map(int, input().split())}
		print(['NO', 'YES'][0 == len(one - two) and one == two])
		
if __name__ == '__main__':
	MySet()