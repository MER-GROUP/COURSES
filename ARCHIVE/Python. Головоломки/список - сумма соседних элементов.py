class Digit:
	def __init__(self):
		pass
	
	@staticmethod	
	def enter():
		return [int(i) for i in input().split()]
	
	@staticmethod	
	def algo(arr):
		res = list()
		for i in range(len(arr)):
			prev = i - 1 if 0 < i else len(arr) - 1
			next = i + 1 if i < len(arr) - 1 else 0
			res.append(arr[prev] + arr[next])
		return str(arr[0]) if 1 == len(arr) else ' '.join(str(i) for i in res)
		
def main():
	arr = Digit.enter()
	print(Digit.algo(arr))
	
if __name__ == '__main__':
	main()