class Digit:
	def __init__(self) -> None:
		pass
	
	@staticmethod
	def hello() -> None:
		# без аргумента возвращает 0.0
		print(float())  # 0.0
		# аргумент может быть строкой
		print(float('4.5'))  # 4.5
		# или числом
		print(float(4.5))  # 4.5
		print(float(-4))  # -4.0
		# экспоненциальная форма записи чисел
		print(float('1e-003'))  # 0.001
		print(float('+1E3'))  # 1000.0
		# минус бесконечность
		print(float('-Infinity'))  # -inf
		# бесконечность
		print(float('Infinity'))  # -inf
		
def main() -> None:
	Digit.hello()
	
if __name__ == '__main__':
	main()