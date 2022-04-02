def Chetvert(x,y):
	if 0<x and 0<y:
		print('Точка в 1 четверти')
	elif 0>x and 0<y:
		print('Точка во 2 четверти')
	elif 0>x and 0>y:
		print('Точка во 3 четверти')
	elif 0<x and 0>y:
		print('Точка во 4 четверти')
	elif 0==x and 0==y:
		print('Точка в центре координат')
	elif 0==x:
		print('Точка лежит на оси Y')
	else:
		print('Точка лежит на оси X')

while True:
	try:
		x=input('x = ')
		if 'q'==x:break
		x=float(x)
		y=float(input('y = '))
	except ValueError:
		print('Некоректный ввод')
		continue
	Chetvert(x,y)