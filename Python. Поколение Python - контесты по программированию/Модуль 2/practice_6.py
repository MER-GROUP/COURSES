class Poker:
	def __init__(self, arr):
		self.__algo(arr)
		
	def __algo(self, arr):
		if arr == arr[: : -1]:
			print('Шулер')
		else:
			arr_sort = sorted(arr)
			if arr_sort[0] == arr_sort[3] or arr_sort[1] == arr_sort[4]:
				print('Каре')
			elif (arr_sort[0] == arr_sort[2] and arr_sort[3] == arr_sort[4]) or (arr_sort[0] == arr_sort[1] and arr_sort[2] == arr_sort[4]):
				print('Фулл Хаус')
			elif self.__is_street(arr, arr_sort):
				print('Стрит')
			elif arr_sort[0] == arr_sort[2] or arr_sort[1] == arr_sort[3] or arr_sort[2] == arr_sort[4]:
				print('Сет')
			elif (arr_sort[0] == arr_sort[1] and arr_sort[2] == arr_sort[3]) or (arr_sort[1] == arr_sort[2] and arr_sort[3] == arr_sort[4]):
				print('Две пары')
			elif arr_sort[0] == arr_sort[1] or arr_sort[1] == arr_sort[2] or arr_sort[2] == arr_sort[3] or arr_sort[3] == arr_sort[4]:
				print('Пара')
			else:
				print('Старшая карта')
				
	def __is_street(self, arr, arr_sort):
		arr_str = ''.join(map(str, arr))
		if '101112131' == arr_str:
			return True
		elif self.__is_less(arr_sort):
			return True
		else:
			return False
			
	def __is_less(self, arr_sort):
		street = [i for i in range(arr_sort[0], arr_sort[0] + len(arr_sort))]
		if arr_sort == street:
			return True
		else:
			return False
		
		
if __name__ == '__main__':
	Poker(list(map(int, input().split())))