def isBin(s):
	try:
		int(s,2)
		return True
	except ValueError:
		return False

while True:
	s=input('Введите двоичное число : ')
	if isBin(s):
		print('Вы ввели двоичное число')
		continue
	elif s=='q':
		break
	else:
		print('Некоректный ввод')