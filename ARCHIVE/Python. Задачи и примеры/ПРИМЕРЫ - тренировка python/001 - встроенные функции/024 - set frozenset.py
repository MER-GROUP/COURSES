class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		# set() создает изменяемое множество
		a = set(range(5))
		# frozenset() создает 
		# неизменяемое множество
		b = frozenset(range(3, 7))
		print(a)
		print(b)
		
		# Добавлять элементы можно 
		# только во множество типа set
		a.add(10)
		print(a)
		
		# пример создания множества из строки
		a = set('abc4')
		print(a)
		
		# Изменяемое множество можно создать 
		# не только вызовом set(),
		a = set([2, 2, 1, 1, 3])
		# также путем использования 
		# фигурных скобок.
		aa = {2, 2, 1, 1, 3}
		# Во множестве не может 
		# быть одинаковых элементов.
		print(a)  # {1, 2, 3}
		print(aa)
		
		# Неизменяемое множество можно 
		# создать только вызовом frozenset()
		b = frozenset([2, 2, 1])
		print(b)
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()