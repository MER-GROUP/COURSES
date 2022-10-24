class Triangle:
	def __init__(self, n):
		arr = [[1]]
		for i in range(n):
			tmp = [1]
			for j in range(1, len(arr[i])):
				tmp += [sum(arr[i][j - 1 : j + 1])]
			tmp += [1]
			arr.append(tmp.copy())
			
		print(arr[n - 1])
		
if __name__ == '__main__':
	Triangle(int(input()))