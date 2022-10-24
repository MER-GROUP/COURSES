class MySet:
	def __init__(self, s1, s2):
		print(('NO', 'YES')[set(s1) == set(s2)])
	
if __name__ == '__main__':
	MySet(input(), input())