class Digit:
	def __init__(self):
		pass
		
	@staticmethod
	def enter():
		return [int(i) for i in input().split()]
		
	@staticmethod
	def algo(arr):
		res = list()
		for i in arr:
			if 1< arr.count(i):
				res.append(i)
		return set(res)
		
def main():
	arr = Digit.enter()
	print(*Digit.algo(arr))
	
if __name__ == '__main__':
	main()