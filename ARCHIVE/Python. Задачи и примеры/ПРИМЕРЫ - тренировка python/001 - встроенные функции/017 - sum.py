class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		a = [1, 2, 3, 4]
		print(a)
		
		# Функция sum() находит общую сумму
		# всех элементов последовательности.
		b = sum(a)
		# Вторым аргументом можно указать 
		# стартовое значение. К нему 
		# добавляется сумма элементов 
		# итерируемого объекта.
		c = sum(a, 5)
		
		print(b, c)
		
		# Итерируемый объект 
		# не обязательно должен быть 
		# списком.
		a = range(10, 20)
		print(sum(a))
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()