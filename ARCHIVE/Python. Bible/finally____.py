def Enter():
	try:
		a=input('Введи число :')
		a=int(a)
		print('a ',a)
		print('a ',type(a))
		if 100<a:
			a=None
			raise ValueError
	except ValueError:
		print('Некоректный ввод')
	finally:
		if 'q'==a:
			a='q'
			return a
		elif type(a)==type(''):
			return None
		else:
			return a
		
d=Enter()
print('d ',d)
print('d ',type(d))