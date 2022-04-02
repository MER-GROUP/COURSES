class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		from math import pi

		a = 10 / 3
		b = 20.7 / 3
		
		# По-умолчанию Python выводит
		# множество знаков после запятой
		# для вещественных чисел
		print(a)
		print(b)
		print(pi)
		
		# round() без второго аргумента
		# округляет до ближайшего целого
		print(round(a))
		print(round(b))
		
		# С помощью второго аргумента
		# указывается количество знаков
		# после запятой
		print(round(a, 2))
		print(round(b, 2))
		print(round(pi, 4))
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()