def isFloat(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

def Enter():
	try:
		d = input('Введи файл : ')
		if 'q' == d:
			pass
		else:
			if d.isdigit() or isFloat(d):
				raise ValueError
	except ValueError:
		print('Введи наименование файла и его расширение')
		d = None
	finally:
		return d
		
def Algo(myStr):
	rashirenie = ('exe', 'png', 'jpg', 'jpeg', 'gif', 'svg')
	myStr = myStr.lower().split('.')
	if 1 < len(myStr):
		if myStr[-1] in rashirenie:
			print('YES')
		else:
			print('NO')
	else:
		print('Not rashirenija')

def Main():
	while True:
		print('---Main---')
		d = None
		while d is None:
			d = Enter()
		if 'q' == d:
			break
		else:
			Algo(d)

Main()