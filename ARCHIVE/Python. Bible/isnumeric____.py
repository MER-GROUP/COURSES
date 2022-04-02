while True:
	n=input('Введите цифры : ')
	if n=='q':
		break
	elif n.isnumeric():
		print('Вы ввели числа')
	else:
		print('Некоректный ввод')