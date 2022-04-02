def beegeek(a, b):
	s = ''
	for i in range(a, b + 1):
		if 0 == i % 3 and 0 == i % 7:
			s += 'BeeGeek '
		elif 0 == i % 7:
			s += 'Geek '
		elif 0 == i % 3:
			s += 'Bee '
		else:
			s += f'{i} '
	return s
			
print(beegeek(14, 21))
print(beegeek(1, 2))
print(beegeek(10, 50))