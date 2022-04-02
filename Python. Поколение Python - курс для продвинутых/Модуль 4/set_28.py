class MySet:
	def __init__(self, a, b):
		print(('NO', 'YES')[set(a).issuperset(b)])
		
if __name__ == '__main__':
	MySet(input(), input())