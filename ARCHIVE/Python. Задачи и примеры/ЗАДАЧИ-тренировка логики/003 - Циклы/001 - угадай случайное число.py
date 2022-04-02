from random import randint

dr=randint(1,100)
cn=0

def Game(d,dr):
	global cn
	cn+=1
	if d<dr:
		print('Загаданное число больше вашего')
		return False
	elif d>dr:
		print('Загаданное число меньше вашего')
		return False
	else:
		print(f'Вы угадали число c {cn} попытки')
		return True

while True:
	try:
		d=input('Угадай число от 1 до 100 :')
		if 'q'==d:break
		d=int(d)
	except ValueError:
		print('Некоректный ввод')
		continue
	else:
		b=Game(d,dr)
		if False==b:
			continue
		else:
			break