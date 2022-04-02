class Football:
	__game_count__ = int(0)
	__game_win__= int(1)
	__game_nobody__ = int(2)
	__game_lose__ = int(3)
	__game_points__ = int(4)
	
	def __init__(self) -> None:
		pass
		
	@staticmethod
	def tire() -> None:
		print('------------------------------')
		
	@staticmethod
	def enter_game_result(n: int) -> list:
		return [input() for _ in range(n)]
		
	#@staticmethod
	def table_game(self, arr: list) -> dict:
		table = dict()
		for i in range(len(arr)):
			tmp = arr[i].split(';')
			for j in range(len(tmp)):
				if 0 == j % 2:
					table[tmp[j]] = [0] * 5
		for i in range(len(arr)):
			tmp = arr[i].split(';')
			if int(tmp[1]) > int(tmp[3]):
					table[tmp[0]][self.__game_count__] += 1
					table[tmp[0]][self.__game_win__] += 1
					table[tmp[0]][self.__game_points__] += 3
					table[tmp[2]][self.__game_count__] += 1
					table[tmp[2]][self.__game_lose__] += 1
					table[tmp[2]][self.__game_points__] += 0
			elif int(tmp[1]) < int(tmp[3]):
					table[tmp[2]][self.__game_count__] += 1
					table[tmp[2]][self.__game_win__] += 1
					table[tmp[2]][self.__game_points__] += 3
					table[tmp[0]][self.__game_count__] += 1
					table[tmp[0]][self.__game_lose__] += 1
					table[tmp[0]][self.__game_points__] += 0
			else:
					table[tmp[0]][self.__game_count__] += 1
					table[tmp[0]][self.__game_nobody__] += 1
					table[tmp[0]][self.__game_points__] += 1
					table[tmp[2]][self.__game_count__] += 1
					table[tmp[2]][self.__game_nobody__] += 1
					table[tmp[2]][self.__game_points__] += 1
		return table
		
	@staticmethod
	def game_result_out(table: dict) -> None:
		for k, v in table.items():
			print(k, ':', sep='', end='')
			print(*v)
		
def main() -> None:
	n = int(input())
	arr = Football.enter_game_result(n)
	#print(arr)
	Football.tire()
	football = Football()
	table = football.table_game(arr)
	football.game_result_out(table)
	football.tire()
	
if __name__ == '__main__':
	main()