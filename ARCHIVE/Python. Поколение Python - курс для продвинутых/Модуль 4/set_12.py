class MySet:
	def __init__(self, s1, s2):
		print(('NO', 'YES')[10 == len(set(s1 + s2))])
	
if __name__ == '__main__':
	MySet(input(), input())