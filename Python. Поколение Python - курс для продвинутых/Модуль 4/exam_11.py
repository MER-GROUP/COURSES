class MySet:
	def __init__(self):
		one = {*map(str, input().split())}
		two = {*map(str, input().split())}
		print(*sorted(one | two))
		
if __name__ == '__main__':
	MySet()