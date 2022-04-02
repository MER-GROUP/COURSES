while True:
	rev=input('Введите строку для '
	                  'реверса (Q - выход): ')
	if rev=='Q' or rev=='q':
		break
	print('Реверс строки = ',
	         ''.join(reversed(rev)))