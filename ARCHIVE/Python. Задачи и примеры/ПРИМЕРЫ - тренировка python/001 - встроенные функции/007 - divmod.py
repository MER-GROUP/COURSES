class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		# Функция divmod() возвращает
		# частное и остаток от деления
		# первого аргумента на второй.
		
		# Для целых чисел
		# результат операции такой же
		# как от (10 // 3, 10 % 3)
		pair1 = divmod(10, 3)  # (3, 1)
		
		# Для вещественных чисел
		# результат: (q, a % b),
		# где q обычно округляется так,
		# как это делает math.floor(a / b),
		# то есть в сторону меньшего целого
		pair2 = divmod(10.5, 3)  # (3.0, 1.5)
		pair3 = divmod(9.9, 5.5)  # (1.0, 4.4)
		
		# результат
		print(pair1)  # (3, 1)
		print(pair2)  # (3.0, 1.5)
		print(pair3)  # (1.0, 4.4)
		
		print('-------------------------------------')
		print(5 // 3)
		print(5 % 3)
		print(divmod(5, 3))
		print('-------------------------------------')
		print(5.5 // 3.3)
		print(5.5 % 3.3)
		print(divmod(5.5, 3.3))
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()