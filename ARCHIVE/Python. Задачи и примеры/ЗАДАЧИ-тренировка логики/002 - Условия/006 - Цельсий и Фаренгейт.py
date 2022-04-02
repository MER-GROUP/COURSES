while True:
	grad=input('Введите температуру в\nЦельсиях 15С или '
	'Фаренгейтах 15F : ')
	if grad=='q': break
	sign=grad[-1]
	grad=grad[0:-1]
	#print(f'grad={grad} sign={sign}')
	try:
		grad=int(grad)
		#if sign!='c':
			#raise ValueError
		log=False
		for i in 'cCfF':
			if sign==i:
				log=True
				break
			#print(f'{i}')
		if False==log:
			raise ValueError
	except ValueError:
		print('Некоректный ввод')
		continue
	if 'c'==sign or 'C'==sign:
		grad=round(grad*(9/5)+32)
		print(f'{grad}F')
	else:
		grad=round((grad-32)*(5/9))
		print(f'{grad}C')