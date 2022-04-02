from random import randint

def Global():
	global count
	count = int()
	global digit_r
	digit_r = int()
	global sto
	sto = int(100)

def is_valid(digit, right = '100'):
	try:
		right = int(right)
		digit = int(digit)
		if not 0 <= digit <= right:
			raise ValueError
		res = True
	except ValueError:
		res = False
	finally:
		return res
		
def Game(digit, digit_r):
	global count
	count += 1
	if digit < digit_r:
		print('Ваше число меньше загаданного, попробуйте еще разок')
		return False
	elif digit > digit_r:
		print('Ваше число больше загаданного, попробуйте еще разок')
		return False
	else:
		print(f'Вы угадали число с {count} попытки, поздравляем!')
		return True
		
def equil(s):
		if 'д' == s.lower(): return True
		else: return False
		
def povtor():
		right = input('Игра гененирует случайное число от 0 до 100, хотите ли вы изменить правый диапозон числа ? (д - да, остпльное нет) : ')
		global digit_r, sto
		while True:
			if equil(right):
				r = input('введите правую границу : ')
				if not is_valid(r, r):
					print('некоректный ввод')
					continue
				else:
					r = int(r)
					digit_r = randint(0, r)
					sto = r
					break
			else:
				sto = 100
				digit_r = randint(0, sto)
				break
		
def Main():
	print('Добро пожаловать в числовую угадайку')
	
	povtor()
	print('digit_r =', digit_r)
	
	digit = int()
	while True:
		digit = input(f'Введите число от 0 до {sto} : ')
		if not is_valid(digit, digit): 
			print(f'А может быть все-таки введем целое число от 0 до {sto}?')
			continue
		else: 
			digit = int(digit)
			if Game(digit, digit_r): 
				game = input('Хотите повторить игру ? (д - да, остальное - нет) : ')
				if equil(game): 
					global count
					count = 0
					povtor()
					print('digit_r =', digit_r)
					continue
				else: break
				
	print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
			
Global()
Main()