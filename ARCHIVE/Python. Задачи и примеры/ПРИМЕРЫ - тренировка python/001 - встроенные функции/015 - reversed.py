class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		a = [1, 2, 3, 4]
		# Функция reversed() возвращает
		# объект-итератор, генерирующий элементы
		# переданной последовательности
		# в обратном порядке.
		b = reversed(a)
		print(b)
		print(list(b))
		
		a = "hello"
		b = reversed(a)
		print(b)
		# Помещаем элементы в список,
		# затем объединяем их в строку.
		print(''.join(list(b)))
		
		a = range(5)
		b = reversed(a)
		print(b)
		print(list(b))
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()