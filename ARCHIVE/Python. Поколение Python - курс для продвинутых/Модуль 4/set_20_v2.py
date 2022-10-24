class MySet:
	def __init__(self, arr):
		st = set()
		for i in arr:
			if i in st:
				print('YES')
			else:
				print('NO')
				st.add(i)
		
if __name__ == '__main__':
	MySet(list(map(int, input().split())))