class Digit:
	def __init__(self, arr):
		#print(len(set(arr)))
		cnt = 1
		for i in range(len(arr) - 1):
			if arr[i] != arr[i + 1]:
				cnt += 1
		print(cnt)
		
if __name__ == '__main__':
	Digit(list(map(int, input().split())))