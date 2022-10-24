class Tribonachi:
	def __init__(self, n):
		a, b, c = 1, 1, 1
		for i in range(n):
			if 3 > i:
				print(a, end=' ')
			else:
				a, b, c = a + b + c, a, b
				print(a, end=' ')
		
if __name__ == '__main__':
	Tribonachi(int(input()))