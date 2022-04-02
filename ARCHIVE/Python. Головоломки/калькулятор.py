class Calc:
	def __init__(self):
		pass
		
	@staticmethod
	def enter():
		return [input() for _ in range(3)]
		
	def __plus__(self, a, b):
		return float(a) + float(b)
		
	def __minus__(self, a, b):
		return float(a) - float(b)
		
	def __division__(self, a, b):
		try:
			return float(a) / float(b)
		except ZeroDivisionError:
			return 'Деление на 0!'
			
	def __multiplication__(self, a, b):
		return float(a) * float(b)
		
	def __mod_ost__(self, a, b):
		try:
			return float(a) % float(b)
		except ZeroDivisionError:
			return 'Деление на 0!'
		
	def __pow__(self, a, b):
		return float(a) ** float(b)
		
	def __div_int__(self, a, b):
		try:
			return float(a) // float(b)
		except ZeroDivisionError:
			return 'Деление на 0!'
			
	def calc(self, a, b, sign):
		if '+' == sign: 
			print(self.__plus__(a, b))
		elif '-' == sign:
			print(self.__minus__(a, b))
		elif '/' == sign:
			print(self.__division__(a, b))
		elif '*' == sign:
			print(self.__multiplication__(a, b))
		elif 'mod' == sign:
			print(self.__mod_ost__(a, b))
		elif 'pow' == sign:
			print(self.__pow__(a, b))
		elif 'div' == sign:
			print(self.__div_int__(a, b))
		
def main():
	calc = Calc()
	a, b, sign = calc.enter()
	calc.calc(a, b, sign)
	
if __name__ == '__main__':
	main()