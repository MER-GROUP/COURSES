class MySet:
	def __init__(self, a, b):
		print(['NO', 'YES'][0 < len(set(a).intersection(b))])
		
if __name__ == '__main__':
	MySet(input(), input())