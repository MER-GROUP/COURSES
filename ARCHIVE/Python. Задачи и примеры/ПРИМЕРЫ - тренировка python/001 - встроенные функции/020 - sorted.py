class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		a = [3, 4, 8, 2, 5, 1]
		# Функция sorted() возвращает 
		# новый отсортированный список
		b = sorted(a)
		print(a)
		print(b)
		
		# С помощью ключа reverse можно
		# отсортировать от большего к меньшему
		c = sorted(a, reverse=True)
		print(c)
		
		a = [(4, 5), (8, 9), (3, 1), (6, 0)]
		# Сортировка по первым элементам 
		# вложенных кортежей
		print(sorted(a))
		# Сортировка по вторым элементам.
		# Именованный key-аргумент 
		# принимает функцию.
		# Ей передается каждый элемент 
		# итерируемого объекта.
		# Сортировка происходит по тому, 
		# что возвращает функция.
		print(sorted(a, key=lambda x: x[1]))
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()