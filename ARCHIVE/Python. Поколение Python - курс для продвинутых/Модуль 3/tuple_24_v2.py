class Tribonachi:
	def __init__(self, n):
		a = b = c = 1
		for i in range(n):
			print(a, end=' ')
			a, b, c = b, c, a + b + c
		
if __name__ == '__main__':
	Tribonachi(int(input()))