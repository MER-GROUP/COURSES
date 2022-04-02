class Triangle:
	def __init__(self):
		pass
	@staticmethod
	def enter():
		return [int(input()) for _ in range(3)]
	@staticmethod
	def square(a, b, c):
		p = (a + b + c) / 2
		return (p * (p - a) * (p - b) * (p - c)) ** 0.5
		
def main():
	a, b, c = Triangle.enter()
	print(Triangle.square(a, b, c))
	
if __name__ == '__main__':
	main()