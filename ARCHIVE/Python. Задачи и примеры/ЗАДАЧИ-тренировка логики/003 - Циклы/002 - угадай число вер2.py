from random import randint

def Enter():
	try:
		a=input('Введи число :')
		a=int(a)
		#print('a ',a)
		#print('a ',type(a))
		if 100<a:
			a=None
			raise ValueError
	except ValueError:
		if 'q'!=a:
			print('Некоректный ввод')
	finally:
		if 'q'==a:
			return 'q'
		elif type(a)==type(''):
			return None
		else:
			return a
			
def ExitGame():
	try:
		a=input('Повторить игру ? (y/n) : ')
		if 'n'!=a and 'y'!=a:
			a=None
			raise ValueError
	except ValueError:
		print('Некоректный ввод')
	finally:
		return a
		
def Game(chi):
		if chi<rnd:
			print('Загаданное число больше')
		elif chi>rnd:
			print('Загаданное число меньше')
		else:
			print(f'Вы угадали число с {cnt} попытки')

'''		
d=Enter()
print('d ',d)
print('d ',type(d))
'''

#def

while True:
	print('Угадай число от 0 до 100')
	chi=0
	cnt=0
	rnd=randint(0,100)
	print('rnd = ',rnd)
	while chi!=rnd:
		chi=Enter()
		#print('chi =',chi)
		if 'q'==chi:
			#print('Вы ввели q')
			break
		elif chi is None:
			continue
		cnt+=1
		Game(chi)
		'''
		if chi<rnd:
			print('Загаданное число больше')
		elif chi>rnd:
			print('Загаданное число меньше')
		else:
			print(f'Вы угадали число с {cnt} попытки')
			#break
		'''
	g=None
	while None==g:
		g=ExitGame()
	if 'n'==g:
		break
	elif 'y'==g:
		continue
			