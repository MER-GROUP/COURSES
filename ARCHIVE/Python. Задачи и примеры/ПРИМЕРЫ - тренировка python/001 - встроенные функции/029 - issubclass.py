class A:
	def __init__(self):
		pass
		
class B(A):
	def __init__(self):
		pass
		
class D(B):
	def __init__(self):
		pass
		
class C:
	def __init__(self):
		pass
		
if __name__ == '__main__':
	def main():
		# issubclass проверяет, является ли
		# один класс подклассом другого
		print(issubclass(B, A))  # True
		print(issubclass(D, A))  # True
		print(issubclass(C, A))  # False
		
		# Класс считается подклассом самого себя
		print(issubclass(C, C))  # True
		
		# Второй аргумент может быть
		# кортежем классов.
		# Чтобы функция вернула истину,
		# достаточно одного соответствия
		print(issubclass(B, (A, C)))  # True
		
		# Также можно проверять наследование
		# встроенных классов
		print(issubclass(list, object))  # True
		
	main()