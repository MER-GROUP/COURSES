class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		class A:
		    p1 = 0


		a = A()
		print(a.p1)  # 0
		
		# С помощью setattr() можно установить
		# новое значение для существующего атрибута
		setattr(a, 'p1', 9)
		# Это эквивалентно a.p1 = 9
		
		print(a.p1)  # 9
		
		# setattr позволяет добавлять
		# объекту-экземпляру новый атрибут
		setattr(a, 'p2', 'Black')
		print(a.p2)  # Black
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()