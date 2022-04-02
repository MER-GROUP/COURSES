from math import pi

def isFloat(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

while True:
	print('Q - выход')
	h=input('Введите высоту цилиндра :')
	if h=='q' or h=='Q':
		break
	r=input('Введите радиус '
	              'основания цилиндра :')
	if r=='q' or r=='Q':
		break
	elif isFloat(h) and isFloat(r):
		h=float(h)
		r=float(r)
		circles=2*pi*r**2
		side=2*pi*r*h
		area=circles+side
		print('Полная площадь '
		          ' поверхности = {}'
		          .format(round(area,2)))
	else:
	       print('Некоректный ввод')
        