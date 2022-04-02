class NOK:
	def __init__(self):
		pass
	
	@staticmethod	
	def nok( a, b):
		c = a * b
		while 0 != a and 0 != b:
			if a > b: a %= b
			else: b %= a
		return c // (a + b)

def main():
	print(NOK.nok(14, 6))

if __name__ == '__main__':
	main()