while True:
	chi=input('Введите число '
	                  '(Q - выход) : ')
	if chi=='Q' or chi=='q':
		break
	elif chi.isdigit():
		print('Вы ввели число : ',chi)
	else:
		print('Некоректный ввод')