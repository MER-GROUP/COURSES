class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		class A:
		    p1 = 3
		    p2 = "Red"
		
		
		a = A()
		# Функция hasattr() проверяет
		# наличие у объекта атрибута
		print(hasattr(a, 'p2'))  # True
		print(hasattr(a, 'p3'))  # False
		
		# Функция getattr() возвращает
		# значение заданного атрибута
		print(getattr(a, 'p1'))  # 3
		# Это эквивалентно print(a.p1)
		
		# Если у объекта нет указанного атрибута,
		# возникнет ошибка
		# print(getattr(a, 'p3')) - AttributeError
		# Выброс исключения можно предотвратить, если
		# сначала проверить наличие атрибута
		if hasattr(a, 'p3'):
		    # В данном случае тело if не выполнится
		    print(getattr(a, 'p3'))
		
		# Также предотвратить ошибку можно
		# с помощью значения по умолчанию
		print(getattr(a, 'p3', 'no attr'))  # no attr
		# Если же атрибут существует,
		# будет возвращено его значение
		print(getattr(a, 'p2', 'no attr'))  # Red
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()