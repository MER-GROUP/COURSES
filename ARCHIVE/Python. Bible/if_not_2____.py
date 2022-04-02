try:
	a, b = input().lower(), input().lower()
	if a and b not in ('красный', 'синий', 'желтый'):
		raise ValueError
except ValueError:
	print('ошибка цвета')