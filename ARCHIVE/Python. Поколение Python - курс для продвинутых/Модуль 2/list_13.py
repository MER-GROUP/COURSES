class Triangle:
	def __init__(self, n):
		arr = list()
		for i in range(n + 1):
			if 0 <= i <= 1:
				arr.append([1 for i in range(i + 1)])
			else:
				tmp = list()
				for j in range(1, i):
					if j < len(arr[i - 1]):
						tmp.append(arr[i -1][j - 1] + arr[i -1][j])
				arr.append([1, *tmp, 1])
				
		print(arr[n] if len(arr) else [1])
		
if __name__ == '__main__':
	Triangle(int(input()))