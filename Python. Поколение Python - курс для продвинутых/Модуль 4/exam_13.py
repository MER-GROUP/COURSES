class MySet:
	def __init__(self, n):
		arr = list()
		for _ in range(n):
			tmp = list()
			m = int(input())
			for _ in range(m):
				tmp.append(input())
			arr.append(tmp)
		print(*sorted(set(arr[0]).intersection(*arr[1:])), sep='\n')
		
if __name__ == '__main__':
	MySet(int(input()))