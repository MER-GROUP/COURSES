class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		a = ['two', 'tree', 'four', 'five']
		
		# Функция enumerate() принимает
		# итерируемый объект или итератор,
		# возвращает итератор, генерирующий кортежи.
		# Первый элемент кортежа - номер элемента,
		# второй - очередной элемент
		# переданного в enumerate() объекта.
		e = enumerate(a)
		for i in e:
		    print(i)
		print(e)
		print('-----')
		
		# По умолчанию счетчик элементов начинается с нуля.
		# Однако стартовое значение можно задать вручную.
		e = enumerate(a, 2)
		for i in e:
		    print(i)
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()