while True:
	try:
		a=input('Введите целое число 1 : ')
		if a=='q': break
		b=input('Введите целое число 2 : ')
		a=int(a)
		b=int(b)
	except ValueError:
		print('Некоректный ввод')
		continue
	try:
		if a%b==0:
			print(f'{a} делится на {b}')
			continue
	except ZeroDivisionError:
		print('На ноль делить нельзя')
		continue
	else:
		print(f'{a} не делится на {b} так как остаток равен {a%b}')