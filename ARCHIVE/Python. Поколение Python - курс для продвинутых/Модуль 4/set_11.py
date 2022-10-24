class MySet:
	def __init__(self, s):
		if len(s) == len(set(s)):
			print('YES')
		else:
			print('NO')
	
if __name__ == '__main__':
	MySet(input())