class Game:
	def __init__(self, timur, ruslan):
		if timur == 'камень' and ruslan == 'камень':
			print('ничья')
		elif timur == 'ножницы' and ruslan == 'ножницы':
			print('ничья')
		elif timur == 'бумага' and ruslan == 'бумага':
			print('ничья')
		elif timur == 'камень' and ruslan == 'ножницы':
			print('Тимур')
		elif timur == 'камень' and ruslan == 'бумага':
			print('Руслан')
		elif timur == 'ножницы' and ruslan == 'бумага':
			print('Тимур')
		elif ruslan == 'камень' and timur == 'ножницы':
			print('Руслан')
		elif ruslan == 'камень' and timur == 'бумага':
			print('Тимур')
		elif ruslan == 'ножницы' and timur == 'бумага':
			print('Руслан')
		
if __name__ == '__main__':
	Game(input(), input())