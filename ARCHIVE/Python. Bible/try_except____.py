while True: 
	try:
		d=input('Введите цел. число : ')
		if d=='q': break
		d=int(d)
	except ValueError:
		print('Некоректный ввод')