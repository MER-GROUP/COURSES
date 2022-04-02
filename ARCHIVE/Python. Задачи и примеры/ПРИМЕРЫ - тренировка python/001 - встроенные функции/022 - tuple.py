class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		# Создается пустой кортеж
		a = tuple()
		
		from_list = [3, 4, 7]
		# Создание кортежа из списка
		b = tuple(from_list)
		
		c = tuple((2, 3, 5))
		# Создать кортеж можно путем использования круглых скобок (без tuple())
		cc = (2, 3, 5)
		
		from_iterator = zip(range(1, 5), range(10, 15))
		# Создание кортежа из итератора
		d = tuple(from_iterator)
		
		# Если кортеж включает один элемент, после него надо поставить запятую.
		one1 = (3,)
		# Иначе это будет тип данных "элемента".
		one2 = (3)
		
		print(a)
		print(b)
		print(c)
		print(cc)
		print(d)
		print(type(one1), type(one2))
		print(tuple('333'))
		print(tuple((333,)))
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()