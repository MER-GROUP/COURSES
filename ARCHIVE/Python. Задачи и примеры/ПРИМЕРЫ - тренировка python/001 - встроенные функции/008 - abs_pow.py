class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		# abs(x) возвращает 
		# абсолютное значение числа.
		a = abs(-5.1)
		# pow(n, e) эквивалентно оператору 
		# возведения в степень: n**e
		b = pow(2, 3)
		c = pow(2, 2.5)
		d = pow(2, -1)
		# pow(n, e, m) эквивалентно 
		# n**e % m
		e = pow(2, 3, 5)

		print(a)
		print(b)
		print(c)
		print(d)
		print(e)
		
		print('-------------------------------------')
		print(2 ** 4)
		print(2 ** 4 % 10)
		print(pow(2, 4))
		print(pow(2, 4, 10))
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()