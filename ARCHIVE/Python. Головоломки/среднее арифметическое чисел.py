class Digit:
	def __init__(self):
		pass	
	@staticmethod
	def enter():
		return [int(input()) for _ in range(2)]
	@staticmethod
	def average(a, b):
		count, sum = [int()] * 2
		for i in range(a, b + 1):
			if 0 == i % 3:
				count += 1
				sum += i
		return sum / count
		
		
def main():
	a, b = Digit.enter()
	print(Digit.average(a, b))
	
if __name__ == '__main__':
	main()