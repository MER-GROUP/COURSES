class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		a = [1, 2, 3, 4]
		b = ('a', 'b', 'c')
		c = {1: 'a', 2: 'b'}
		d = range(8)
		e = "hello"
		
		# len() возвращает количество
		# элементов объекта.
		# Аргумент может быть последовательностью
		# или коллекцией.
		print(a, ' -', len(a))
		print(b, ' -', len(b))
		print(c, ' -', len(c))
		print(d, ' -', len(d))
		print(e, ' -', len(e))
		
		print('------------------------------------')
		print(d)
		print(*d)
		print(type(d))
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()