class Zodiak(dict):
	def __init__(self, year):
		self.year = year
		self.my_dict = {2000: 'Дракон', 2001: 'Змея', 2002: 'Лошадь', 2003: 'Овца', 2004: 'Обезьяна', 2005: 'Петух', 2006: 'Собака', 2007: 'Свинья', 2008: 'Крыса', 2009: 'Бык', 2010: 'Тигр', 2011: 'Заяц'}
		self.__zodiak__()
		
	def __zodiak__(self):
		year_2000 = 2000
		i = int()
		while True:
			if self.year < year_2000:
				year_2000 -= 1
				i -= 1
				if -1 == i:
					i = 11
			elif self.year > year_2000:
				year_2000 += 1
				i += 1
				if 12 == i:
					i = 0
			else:
				break
		#print('i =', i)

		it = iter(self.my_dict.values())
		for j in range(i):
			next(it)
		print(next(it))
		
if __name__ == '__main__':
	Zodiak(int(input()))