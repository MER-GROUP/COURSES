def Treug(a,b,c):
	if a+b>=c and a+c>=b and c+b>=a:
		print('Треугольник есть')
	else:
		print('Треугольника нет')

while True:
	try:
		a=input('a = ')
		if 'q'==a: break
		a=float(a)
		b=float(input('b = '))
		c=float(input('c = '))
	except ValueError:
		print('Некоректный ввод')
		continue
	Treug(a,b,c)