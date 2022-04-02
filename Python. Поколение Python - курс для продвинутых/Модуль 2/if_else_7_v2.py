class Game:
	def __init__(self, timur, ruslan):
		var = ['камень', 'ножницы', 'бумага']
		ans = ['ничья', 'Руслан', 'Тимур']
		print(ans[var.index(timur) - var.index(ruslan)])
		
if __name__ == '__main__':
	Game(input(), input())