from math import pi,pow

def isFloat(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

while True:
	print('Q - выход')
	r=input('Введите радиус '
	              'окружности :')
	if r=='q' or r=='Q':
		break
	elif r.isdigit() or isFloat(r):
		r=float(r)
		l=2*pi*r
		s=pi*pow(r,2)
		print(f'Длина окружности {l:.2f}\n'
		         f'площадь круга {s:.2f}')
	else:
		print('Некоректный ввод')