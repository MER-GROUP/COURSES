class Zodiak(dict):
	def __init__(self, year):
		self.year = year
		self.my_list = ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц']
		self.__zodiak__()
		
	def __zodiak__(self):
		print(self.my_list[self.year % 12 - 8])
		
if __name__ == '__main__':
	Zodiak(int(input()))