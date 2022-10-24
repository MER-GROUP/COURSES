class Timur:
	def __init__(self):
		n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
		i = n + m + k
		j = x + y + z
		print(3 * (t - i) + 2 * j)
		print(2 * i - j - 3 * t)
		print(a + i - j - t)
		
if __name__ == '__main__':
	Timur()