def isFloat(a):
	try:
		float(a)
		return True
	except ValueError:
		return False

while True:
	a=input('Введите дробное '
	               'число (Q - выход) : ')
	if a=='q' or a=='Q':
		break
	#elif a.isdigit()
	#elif type(a)==int or type(a)==float:
	#elif a.isnumeric():
	elif a.isdigit() or isFloat(a):
		print('a =',round(float(a),2))
		print(f'a = {round(float(a),2)}')
		print(f'a = {float(a):.2f}')
		print('a = {0:.2f}'.format(float(a)))
		print('a = %.2f'%float(a))
		print('a = %.2s'%a)
	else:
		print('Некоректный ввод')
		continue