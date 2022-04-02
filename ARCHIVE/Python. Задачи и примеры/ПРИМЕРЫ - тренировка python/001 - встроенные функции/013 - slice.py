class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		a = [1, -2, 4, 9, -6, 5, -1]
		print(a)
		print('----------')
		
		# Вызов slice() возвращает 
		# объект типа slice, который имеет 
		# три свойства: start, stop, step
		b = slice(0, len(a), 3)
		print(b)
		# Объекты типа slice можно использовать 
		# для взятия срезов из последовательностей.
		print(a[b])
		print('----------')
		
		# Можно передать только 
		# один аргумент - stop.
		c = slice(3)
		print(c)
		# В этом случае будет срез 
		# от 0 до stop с шагом 1.
		print(a[c])
		print('----------')
		
		# Можно указать два аргумента
		# - start и stop.
		d = slice(2, 5)
		print(d)
		print(a[d])
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()