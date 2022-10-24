class MySet:
	def __init__(self, s):
		print(('NO', 'YES')[len(s) == len(set(s))])
	
if __name__ == '__main__':
	MySet(input())