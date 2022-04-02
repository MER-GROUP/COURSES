class MySet:
	def __init__(self, a, b):
		print(('YES', 'NO')[set(a).isdisjoint(b)])
		
if __name__ == '__main__':
	MySet(input(), input())