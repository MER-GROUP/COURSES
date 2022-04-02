def Year(y):
	if 0!=y%4:
		print('Год обычный')
	elif 0==year%100:
		if 0==year%400:
			print('Год високосный')
		else:
			print('Год обычный')
	else:
		print('Год високосный')

while True:
	try:
		year=input('Введите год : ')
		if 'q'==year:break
		year=int(year)
	except ValueError:
		print('Некоректный ввод')
		continue
	else:
		Year(year)