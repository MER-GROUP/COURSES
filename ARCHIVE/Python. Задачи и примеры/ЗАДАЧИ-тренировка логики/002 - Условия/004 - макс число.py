def isFloat(f):
	try:
		float(f)
		return True
	except ValueError:
		return False

while True:
	a=input('Число 1 : ')
	if a=='q':
		break
	b=input('Число 2 : ')
	c=input('Число 3 : ')
	if isFloat(a) and isFloat(b) and isFloat(c): 
		a=float(a)
		b=float(b)
		c=float(c)
		if a>=b and a>=c:
			print('max =',a)
		elif b>=c and b>=a:
			print('max =',b)
		else:
			print('max =',c)
		print('---------')
		if b<=a>=c:
			print('max =',a)
		elif a<=b>=c:
			print('max =',b)
		else:
			print('max =',c)
	else:
		print('Некоректный ввод')
	