def isFloat(f):
	try:
		float(f)
		return True
	except:
		return False
		
while True:
	d=input('Введите число : ')
	if d=='q':
		break
	elif d.isdigit() or isFloat(d):
		d=float(d)
		if d<0:
			print('Число oтрицательное')
		elif d>0:
			print('Число положительное')
		else:
			print('Ноль')
	else:
		print('Некоррнктный ввод')