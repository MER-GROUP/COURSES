while True:
	s=input('Введите буквы : ')
	if s=='q':
		break
	elif s.isalpha():
		print('Введены буквы')
		continue
	else:
		print('Введена солянка')