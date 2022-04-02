class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		# Создается последовательность от нуля
		# до заданного числа, не включая его
		a = range(10)
		# Вызов range() возвращает объект типа range
		print(a)
		# Цикл for превращает объект range в итератор
		for i in a:
		    print(i, end=' ')
		
		print("\n------")
		
		# от -5 до 4 включительно
		a = range(-5, 5)
		print(a)
		# преобразуем объект range в список
		print(list(a))
		
		print("------")
		
		# Третим аргументом задается шаг
		a = range(1, 11, 2)
		print(a)
		print(list(a))
		
		print("------")
		
		# Отрицательный шаг для последовательностей
		# от большего к меньшему
		a = range(11, 1, -3)
		print(a)
		print(list(a))
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()