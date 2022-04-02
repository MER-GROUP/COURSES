class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		# chr(i) принимает
		# числовой код символа в Unicode,
		# возвращает символ
		print(chr(97))  # a
		print(chr(20049))  # 乑
		
		# ord(c) принимает символ,
		# возвращает его номер в Unicode
		print(ord('Z'))  # 90
		print(ord('乑'))  # 20049
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()