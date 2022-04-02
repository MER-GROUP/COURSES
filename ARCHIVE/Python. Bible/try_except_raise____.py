while True:
	try:
		s=input('введи полож число : ')
		if 'q'==s: break
		sign=s[0]
		s=int(s)
		if '-'==sign:
			raise ValueError
		else:
			print('Положительное число')
	except ValueError:
		print('Некоректный ввод')