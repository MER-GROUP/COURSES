class Digit:
	def __init__(self):
		pass
	@staticmethod
	def is_prime(d):
		for i in range(2, int((d + 1) ** 0.5)):
			if 0 == d % i:
				return False
		else: return True if not 1 == d else False
		
def main():
	print(Digit.is_prime(1))
	print(Digit.is_prime(2))
	print(Digit.is_prime(17))
	print(Digit.is_prime(57))
	print(Digit.is_prime(103))
	
if __name__ == '__main__':
	main()