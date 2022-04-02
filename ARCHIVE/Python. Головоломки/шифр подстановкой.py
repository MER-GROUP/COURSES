class Shifr:
	def __init__(self) -> None:
		pass
		
	@staticmethod
	def enter() -> list:
		return [input() for _ in range(4)]
		
	@staticmethod
	def dict_keys(key_deshifr: list, key_shifr: list) -> tuple:
		dict_key_shifr = dict(zip(key_shifr, key_deshifr))
		dict_key_deshifr = dict(zip(key_deshifr, key_shifr))
		return dict_key_shifr, dict_key_deshifr
		
	@staticmethod
	def shifr(to_shifr: str, dict_key_shifr: dict) -> str:
		res = str()
		for i in to_shifr:
			res += dict_key_shifr.get(i)
		return res
		
	'''
	@staticmethod
	def deshifr(to_deshifr: str, dict_key_deshift: dict) -> str:
		res = str()
		for i in to_deshifr:
			res += dict_key_deshift.get(i)
		return res
	'''
	@staticmethod
	def deshifr(to_deshifr: str, dict_key_deshift: dict) -> str:
		return Shifr.shifr(to_deshifr, dict_key_deshift)
		
def main() -> None:
	key_shifr, key_deshifr, to_shifr, to_desgifr = Shifr.enter()
	dict_key_shifr, dict_key_deshifr = Shifr.dict_keys(key_deshifr, key_shifr)
	#print(dict_key_shifr)
	#print(dict_key_deshifr)
	print(Shifr.shifr(to_shifr, dict_key_shifr))
	print(Shifr.deshifr(to_desgifr, dict_key_deshifr))
	
if __name__ == '__main__':
	main()