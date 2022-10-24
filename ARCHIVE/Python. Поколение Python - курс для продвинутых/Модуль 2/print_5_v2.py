class Zodiak(dict):
	def __init__(self, year):
		self.year = year
		self.my_list = ['Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна']
		self.__zodiak__()
		
	def __zodiak__(self):
		while self.year > 12:
			self.year -= 12
		print(self.my_list[self.year - 1])
		
if __name__ == '__main__':
	Zodiak(int(input()))