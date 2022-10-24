class Game:
	def __init__(self, tim, rus):
		if tim == rus:
			print('ничья')
		else:
			if tim == 'камень' and rus == 'ящерица' or tim == 'камень' and rus == 'ножницы':
				print('Тимур')
			elif rus == 'камень' and tim == 'ящерица' or tim == 'камень' and rus == 'ножницы':
				print('Руслан')
			elif tim == 'ножницы' and rus == 'бумага' or tim == 'ножницы' and rus == 'ящерица':
				print('Тимур')
			elif rus == 'ножницы' and tim == 'бумага' or tim == 'ножницы' and rus == 'ящерица':
				print('Руслан')
			elif tim == 'бумага' and rus == 'камень' or tim == 'бумага' and rus == 'Спок':
				print('Тимур')
			elif rus == 'бумага' and tim == 'камень' or tim == 'бумага' and rus == 'Спок':
				print('Руслан')
			elif tim == 'ящерица' and rus == 'бумага' or tim == 'ящерица' and rus == 'Спок':
				print('Тимур')
			elif rus == 'ящерица' and tim == 'бумага' or tim == 'ящерица' and rus == 'Спок':
				print('Руслан')
			elif tim == 'Спок' and rus == 'ножницы' or tim == 'Спок' and rus == 'камень':
				print('Тимур')
			else:
				print('Руслан')
		
if __name__ == '__main__':
	Game(input(), input())