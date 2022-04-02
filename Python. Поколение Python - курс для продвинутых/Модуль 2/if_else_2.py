class Didit:
	def __init__(self, arr):
		cnt = int()
		for i in range(1, len(arr)):
			if arr[i] > arr[i - 1]:
				cnt += 1
		print(cnt)
		
if __name__ == '__main__':
	arr = [int(i) for i in input().split()]
	Didit(arr)