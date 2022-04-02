class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		# Все числа - True, кроме нуля
		print(bool(15))  # True
		print(bool(0))  # False
		
		# Пустая строка - False
		print(bool("hello"))  # True
		print(bool(""))  # False
		
		# Пустая последовательность - False
		print(bool([1, 2, 3]))  # True
		print(bool([]))  # False
		
		# Сложение
		print(True + True + True) # 3
		print(True + True - True) # 3
		print(-True - True - True) # 3
		print(False + False + False) # 0
		print(-False - False - False) # 0
		print(True + False + True + False) # 2
		print(True * True * True) # 1
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()