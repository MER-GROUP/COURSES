def Enter():
	try:
		digit = input('Введи целое число : ')
		if 'q' == digit:
			pass
		elif '0' == digit[0] and 1 < len(digit) or digit[0 : 2] in ('-0', '+0') and 2 < len(digit):
			raise ValueError
		else:
			digit = int(digit)
	except ValueError:
		print('Некоректный ввод !')
		digit = None
	finally:
		return digit
		
def ReverseOne(digit):
	rev = 0
	while 0 < digit:
		ost = digit % 10
		rev += ost
		digit //=10
		rev *= 10
	rev //=10
	print(rev)
	
def ReverseTwo(digit):
	rev = 0
	while 0 < digit:
		ost = digit % 10
		rev *= 10
		rev +=ost
		digit //= 10
	print(rev)
	
def ReverseTree(digit):
	rev = str(digit)
	rev = ''.join(reversed(rev))
	print(rev)

def Main():
	while True:
		print('---Main---')
		digit = None
		while digit is None:
			digit = Enter()
		if 'q' == digit:
			break
		ReverseOne(digit)
		ReverseTwo(digit)
		ReverseTree(digit)
		
Main()