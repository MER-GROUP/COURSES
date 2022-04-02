#############################
# input_int() or input_int(prefix=True, null=False) :
# правильный ввод чисел если впепеди есть префикс и нет нулей :
# correct number input if prefix = True, null = False :
# 123, +9, - 45, 0 -0, +0
# неправильный ввод чисел :
# incorrect number input :
# 0987, +054, 000, -03, gfdt, _&$#g
#############################
# добавить вариант без префикса тоесть число без знака + и -
# вариант что если впереди много нулей вести себя как int(input())
#############################
def input_int(text = '', prefix = True, null = False):
	try:
		digit = input(text)
		if digit[ : 2] in ('+0', '-0') and 2 < len(digit) and prefix and not null:
			raise Exception
		elif digit[0] in ('+', '-') and 1 < len(digit) and not prefix:
			raise Exception
		elif '0' == digit[0] and 1 < len(digit) and not null:
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
def is_equal(text1, text2, lower = True):
	if lower:
		text1 = text1.lower()
		text2 = text2.lower()
	if text1 == text2: return True
	else: False
#############################