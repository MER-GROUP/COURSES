from math import sqrt

count = 0

def Enter():
	try:
		digit = input()
		if 'q' == digit: pass
		elif '0' == digit[0] and 1 < len(digit) or digit[0:2] in ('-0', '+0') and  2 < len(digit):
			#print(len(digit))
			raise ValueError
		else: digit = int(digit)
	except ValueError:
		print('Некоректный ввод')
		digit = None
	finally:
		return digit
		
def Count(digit):
	if digit in (-1, 0, 1):
		print('Число 0, 1, -1 не простые и не состпвные')
	else:
		global count
		check = False
		for i in range(2, int(sqrt(digit)) + 1):
			if 0 == digit % i:
				check = True
				break
		if check: count += 1

def Main():
	while True:
		#print('---Main---')
		digit = None
		while digit is None:
			digit = Enter()
		if 'q' == digit: 
			print(count)
			break
		else:
			Count(digit)
	
Main()