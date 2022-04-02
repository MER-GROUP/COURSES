class Arr:
	def __init__(self):
		pass
	@staticmethod
	def shift(arr, it):
		if 0 > it:
			it = abs(it)
			for _ in range(it):
				el = arr.pop(0)
				arr.append(el)
		else:
			for _ in range(it):
				el = arr.pop()
				arr.insert(0, el)

def main():
	arr = [i for i in range(10)]
	print(arr)
	Arr.shift(arr, -3)
	print(arr)
	Arr.shift(arr, 3)
	print(arr)
	
if __name__ == '__main__':
	main()