class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		# Создается пустой список
		a = list()
		
		tuple_iterable = (1, 2, 3)
		# Кортеж преобразовывается в список
		b = list(tuple_iterable)
		
		range_iterable = range(3, 8)
		# Объект range преобразовывается в список
		c = list(range_iterable)
		
		str_iterable = "hello"
		# Строка преобразуется в список символов
		d = list(str_iterable)
		
		another_iter = filter(lambda x: x % 6 == 0, range(55))
		print(type(another_iter))
		# С помощью list() можно получить список генерируемых итератором элементов
		e = list(another_iter)
		
		print(a)
		print(b)
		print(c)
		print(d)
		print(e)
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()