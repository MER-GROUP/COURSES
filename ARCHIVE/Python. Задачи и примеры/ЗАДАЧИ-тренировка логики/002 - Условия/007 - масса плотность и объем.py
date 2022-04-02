def isFloat(f):
	try:
		float(f)
		return True
	except ValueError:
		return False

def Massa():
	while True:
		try:
			d=float(input('введите d : '))
			v=float(input('введите v : '))
			break
		except ValueError:
			print('Некоректный ввод')
			continue
	return d*v
	
def Plotnost():
	while True:
		try:
			m=float(input('введите m : '))
			v=float(input('введите v : '))
			break
		except ValueError:
			print('Некоректный ввод')
			continue
	return m/v
	
def Volume():
	while True:
		try:
			m=float(input('введите m : '))
			d=float(input('введите d : '))
			break
		except ValueError:
			print('Некоректный ввод')
			continue
	return m/d

result=None

while True:
	flag=input('Type - m, d, v : ')
	if 'q'==flag:break
	check=False
	for i in 'mdvMDV':
		if flag==i:
			check=True
			break
	if False==check:
		print('Некоректный ввод')
		continue
	if 'm'==flag or 'M'==flag:
		print('m')
		result=Massa()
		#print(f'{result:.2f}')
	elif 'd'==flag or 'D'==flag:
		print('d')
		result=Plotnost()
		#print(f'{result:.2f}')
	else:
		print('v')
		result=Volume()
		#print(f'{result:.2f}')
	print(f'{result:.2f}')