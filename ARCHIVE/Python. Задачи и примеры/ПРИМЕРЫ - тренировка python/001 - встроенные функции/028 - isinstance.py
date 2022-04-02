class A:
	def __init__(self):
		pass
		
class B(A):
	def __init__(self):
		pass
		
class C:
	def __init__(self):
		pass
		
if __name__ == '__main__':
	def main():
		obj = B()
		# Функция isinstance проверяет
		# принадлежность объекта классу
		print(isinstance(obj, B))  # True
		print(isinstance(obj, C))  # False
		# isinstance поддерживает наследование
		print(isinstance(obj, A))  # True
		# Также проверить тип объекта можно
		# с помощью type
		print(type(obj) == B)  # True
		# Однако type не учитывает наследование
		print(type(obj) == A)  # False
		
		print()
		# Можно проверять принадлежность
		# объекта одному классу из кортежа
		print(isinstance(obj, (B, C, A)))  # True
		# isinstance также работает
		# со встроенными классами
		print(isinstance(obj, (B, list)))  # True
		print()
		
		obj2 = {1, 2, 5}
		print(type(obj2) == set)  # True
		print(isinstance(obj2, set))  # True
		print(isinstance(obj2, (list, tuple)))  # False
		
	main()