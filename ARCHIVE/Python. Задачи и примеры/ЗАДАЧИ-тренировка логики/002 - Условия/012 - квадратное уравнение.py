from math import sqrt

def Uravnenie(a,b,c):
	d=b**2-4*a*c
	if 0<d:
		x1=(-b+sqrt(d))/(2*a)
		x2=(-b-sqrt(d))/(2*a)
		print(f'x1 = {x1:.2f} x2 = {x2:.2f}')
		print()
	elif 0==d:
		x1=-b/(2/a)
		print(f'x1 = {x1:.2f}')
		print()
	else:
		print('нет корней')
		print()

while True:
	try:
		a=input('a = ')
		if 'q'==a:break
		a=float(a)
		b=float(input('b = '))
		c=float(input('c = '))
	except ValueError:
		print('некоректный ввод')
		print()
		continue
	else:
		print()
		Uravnenie(a,b,c)