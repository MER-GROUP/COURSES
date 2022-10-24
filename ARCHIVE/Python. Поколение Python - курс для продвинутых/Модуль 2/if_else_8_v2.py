class Game:
	def __init__(self, timur, ruslan):
		var = ['ножницы', 'бумага', 'камень', 'ящерица', 'Спок']
		ans = ['ничья', 'Руслан', 'Тимур', 'Руслан', 'Тимур']
		print(ans[var.index(timur) - var.index(ruslan)])
		
if __name__ == '__main__':
	Game(input(), input())