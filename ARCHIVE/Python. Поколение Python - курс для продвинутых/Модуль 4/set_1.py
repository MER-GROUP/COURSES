class Timur:
	def __init__(self):
		n, m, k, x, y, z = [int(input()) for _ in range(6)]
		k = k - y
		m = m - y - x
		n = n - x
		print(n + m + k + y + x + z)
		
if __name__ == '__main__':
	Timur()