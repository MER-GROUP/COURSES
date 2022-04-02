#############################
# input_int() :
# правильный ввод чисел :
# correct number input :
# 123, +9, - 45, 0 -0, +0
# неправильный ввод чисел :
# incorrect number input :
# 0987, +054, 000, -03, gfdt, _&$#g
# добавить вариант без префикса тоесть число без знака + и -
# вариант что если впереди много нулей вести себя как int(input())
#############################
def input_int(text = ''):
	try:
		digit = input(text)
		if '0' == digit[0] and 1 < len(digit):
			raise Exception
		elif digit[ : 2] in ('+0', '-0') and 2 < len(digit):
			raise Exception
		else:
			digit = int(digit)
	except (Exception, ValueError):
		digit = None
	finally:
		return digit
#############################
def is_input_int(digit):
	pass
#############################
def check(text1, text2, lower = True):
	if lower:
		text1 = text1.lower()
		text2 = text2.lower()
	if text1 == text2: return True
	else: False
#############################