class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		# Десятичное число переводится
		# в двоичную систему счисления
		print(bin(30))
		# в восьмеричную
		print(oct(30))
		# в шестнадцатеричную
		print(hex(30))
		
		# Один из способов избавиться от префиксов
		print(format(30, 'b'))
		print(format(30, 'o'))
		print(format(30, 'x'))
		print(format(30, 'X'))
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()