class Nok:
	def __init__(self):
		pass
	@staticmethod
	def enter():
		return [int(input()) for _ in range(2)]
	@staticmethod
	def nok_algo(a, b):
		c = a * b
		while 0 != a and 0 != b:
			if a > b: a %= b
			else: b %= a
		return c // (a + b)
	@staticmethod
	def nok(a, b):
		i = 1
		while True:
			if 0 == i % a and 0 == i % b:
				return i
			i += 1
		
def main():
	a, b = Nok.enter()
	#print(Nok.nok_algo(a, b))
	print(Nok.nok(a, b))
	
if __name__ == '__main__':
	main()