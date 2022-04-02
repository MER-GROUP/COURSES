class MySet:
	def __init__(self, arr):
		n, m, k, p = arr
		print(n - ((m - p) + (k - p) + p))
		
if __name__ == '__main__':
	MySet([int(input()) for i in range(4)])