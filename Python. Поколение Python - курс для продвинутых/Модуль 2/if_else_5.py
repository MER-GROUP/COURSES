class Digit:
	def __init__(self, arr):
		#print(len(set(arr)))
		cnt = 1
		for i in range(1, len(arr)):
			if arr[i - 1] < arr[i]:
				cnt += 1
		print(cnt)
		
if __name__ == '__main__':
	Digit(list(map(int, input().split())))