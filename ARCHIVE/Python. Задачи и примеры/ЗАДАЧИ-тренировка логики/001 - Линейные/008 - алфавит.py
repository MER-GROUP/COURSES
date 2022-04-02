while True:
	a=input('Введите одну букву'
	               'из алфавита (quit - выход) :')
	if a=='quit' or a=='QUIT':
		break
	elif False==a.isalpha():
		print('Нужно вводить буквы')
		continue
	elif len(a)>1:
		print('Введи одну букву')
		continue
	else:
		a=ord(a)
		x1=ord('a')
		res=a-x1+1
		print('res =',res)