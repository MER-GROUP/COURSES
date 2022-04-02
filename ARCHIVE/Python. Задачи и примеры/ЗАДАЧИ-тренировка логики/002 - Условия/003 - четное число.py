while True:
	d=input('Введите целое число : ')
	if d=='q':
		break
	elif d.isdigit():
		d=int(d)
		if (d%2)==0:
			print('Число четное')
		else:
			print('Число нечетное')
	else:
		print('Некоректный ввод')