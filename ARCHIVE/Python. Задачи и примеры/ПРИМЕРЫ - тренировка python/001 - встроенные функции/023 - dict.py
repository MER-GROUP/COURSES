class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
            # Вызов dict() без аргументов 
            # создает пустой словарь
            a = dict()
            # Произвольное количество аргументов. 
            # Каждый аргумент состоит из ключа, 
            # которому присваивается значение.
            b = dict(x=1, y=2)
            
            key_list = ['x', 'y']
            value_list = [1, 2]
            # Здесь в dict() передается объект-итератор, 
            # генерирующий кортежи (см. функцию zip()).
            c = dict(zip(key_list, value_list))
            
            # В dict() можно передать 
            # уже готовый словарь.
            d = dict({'x': 1, 'y': 2})
            # Однако проще без dict().
            dd = {'x': 1, 'y': 2}
            
            tuple_list = [('x', 1), ('y', 2)]
            # Передача в dict() итерируемого объекта, 
            # каждый элемент которого - 
            # кортеж из двух элементов.
            e = dict(tuple_list)
            
            print(a)
            print(b)
            print(c)
            print(d)
            print(dd)
            print(e)
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()