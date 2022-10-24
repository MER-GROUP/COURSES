class MySet:
	def __init__(self, m, n):
		one = set()
		two = set()
		for _ in range(m + n):
			fio = input()
			if not fio in one:
				one.add(fio)
			else:
				two.add(fio)
		print('NO' if 0 == len(one.symmetric_difference(two)) else len(one.symmetric_difference(two)))
		
if __name__ == '__main__':
	MySet(int(input()), int(input()))