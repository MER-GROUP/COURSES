class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		a = int('34')
		b = int(3.8)
		c = int('111001', 2)
		d = int('12', 8)
		e = int('ff', 16)
		f = int('1G', 25)
		print(a)
		print(b)
		print(c)
		print(d)
		print(e)
		print(f)
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()