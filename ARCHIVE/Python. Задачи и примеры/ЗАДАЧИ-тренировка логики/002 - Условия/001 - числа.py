def isFloat(f):
	try:
		float(f)
		return True
	except ValueError:
		return False

while True:
	d=input('Введите число (q - выход) : ')
	if d=='q':
		break
	elif d.isdigit() or isFloat(d):
		print('Число')
		if d.isnumeric():
			print('положительное')
		else:
			if d[0]=='-':
				print('отрицательное')
			else:
				print('положительное')
	else:
		print('Некоректный ввод')