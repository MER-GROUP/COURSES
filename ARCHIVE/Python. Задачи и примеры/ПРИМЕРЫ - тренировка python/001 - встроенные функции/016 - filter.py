class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		a = ['one', '', 'three', '', 'five', 'six']
		print('---1---')	
		# Функция filter() создает объект-итератор,
		# в который попадают все элементы из переданного
		# в нее итерируемого объекта или итератора (a),
		# для которых функция, указанная в качестве
		# первого аргумента, возвращает истину.
		# Вместо имени функции может быть None.
		# В этом случае будут исключены false-элементы.
		b = filter(None, a)
		for i in b:
		    print(i)
		print('---2---')
		
		def big_len(s):
		    return len(s) > 3
		
		b = filter(big_len, a)
		for i in b:
		    print(i)
		
		print('---3---')
		
		# чаще в filter() вместо обычной функции
		# передают lambda-выражение
		b = filter(lambda x: len(x) > 3, a)
		for i in b:
		    print(i)
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()