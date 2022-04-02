class Digit:
	def __init__(self, arr):
		self.arr_end = arr.pop() if 1 == len(arr) % 2 else str()
		i = int()
		while i < len(arr):
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
				i += 2
		#print(self.arr_end)
		arr.extend(list(self.arr_end))
		print(*arr)
		
if __name__ == '__main__':
	Digit(input().strip().split())