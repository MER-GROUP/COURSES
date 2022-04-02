def AcsiDigit():
	return  {0 : 9471, 1 : 10102, 2 : 10103, 3 : 10104, 4 : 10105, 5 : 10106, 6 : 10107, 7 : 10108, 8 : 10109, 9 : 10110}
	
def InputDigitStr():
	try:
		d = input('введи число : ')
		if Check(d): pass
		elif not d.isdigit(): raise Exception
	except Exception:
		print('некоректный ввод')
		d = None
	finally:
		return d
		
def Check(s):
	if 'q' == s: return True
	else: return False
	
def ConverDigitToAcsi(digits, d):
	for i in d:
		print(chr(digits[int(i)]), end='')
	print()

def Main():
	while True:
		print('-----Main()-----')
		d = None
		while d is None:
			d = InputDigitStr()
		if Check(d): break
		else: ConverDigitToAcsi(AcsiDigit(),d)
		
Main()