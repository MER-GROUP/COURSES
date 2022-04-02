x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if x1 and x2 and  y1 and y2 in (range(1, 8 + 1)):
	print('x1, x2, y1, y2 в диапозоне от 1 до 8')
	if x1 == x2 and y1 + 1 == y2 or x1 == x2 and y1 - 1 == y2 or y1 == y2 and x1 + 1 == x2 or y1 == y2 and x1 - 1 == x2:
		print('Ход сделан на одну клетку')
	elif x1 == x2 and y1 < y2 or x1 == x2 and y1 > y2 or y1 == y2 and x1 < x2 or y1 == y2 and x1 > x2:
		print('Ход сделан')
	else:
		print('Нет хода')
else:
	print('x1, x2, y1, y2 не в диапозоне от 1 до 8')