class MySet:
	def __init__(self, n):
		st = set()
		for _ in range(n):
			for c in input().lower():
				st.add(c)
		print(len(set(st)))
		
if __name__ == '__main__':
	MySet(int(input()))