class Coordinat:
	def __init__(self) -> None:
		self.__coord__ = dict(север = 0, запад = 0, юг = 0, восток = 0)
		
	#@staticmethod
	def enter(self, n: int) -> dict:
		for _ in range(n):
			tmp = input().lower().split()
			self.__coord__[tmp[0]] += int(tmp[1])
		return self.__coord__
		
	@staticmethod
	def result(coord: dict) -> tuple:
		x = coord.get('восток') - coord.get('запад')
		y = coord.get('север') - coord.get('юг')
		return x, y
		
def main() -> None:
	n = int(input())
	coordinat= Coordinat()
	coord = coordinat.enter(n)
	#print(coord)
	print(*coordinat.result(coord))
	
if __name__ == '__main__':
	main()