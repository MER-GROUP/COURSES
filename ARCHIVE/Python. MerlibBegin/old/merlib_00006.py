#############################
# input_int()
# функция для проверки что число целое
# function for checking that a number is an integer
#############################
# настройки : 
# settings : 
# 1) если истина то всегда возвращается само целое число, иначе возвращается None
# 1) if true return int value, else None
# 2) text = '' - описание запроса
# 2) text = '' - request description
# 3) prefix = True or False -  проверяет наличие знаков + и - перед целым числом
# 3) prefix = True or False -  checks for the presence of + and - signs before an integer
# 4) null = True or False - проверяет наличие нулей перед целым число
# 4) null = True or False - checks for zeros before an integer
#############################
# примеры :
# examples :
#############################
# input_int('введи число') аналогично input('введи число')
# input_int('введи число') analogically input('введи число')
#############################
# input_int() or input_int(prefix=True, null=False) :
# правильный ввод чисел если впепеди есть префикс и нет нулей :
# correct number input if prefix = True, null = False :
# 123, +9, - 45, 0 -0, +0
# неправильный ввод чисел :
# incorrect number input :
# 0987, +054, 000, -03, gfdt, _&$#g, 8.5
#############################
# input_int(prefix=False, null=False) :
# правильный ввод чисел если впепеди нет префикса и нет нулей :
# correct number input if prefix = False, null = False :
# 9, 56, 100
# неправильный ввод чисел :
# incorrect number input :
# -0, +0, -7, +8, 00, -008, +098, gf, &$#, 7.4
#############################
# input_int(prefix=False, null=True) :
# правильный ввод чисел если впепеди нет префикса но есть нули, альтернатива команды int(input()) :
# correct number input if prefix = False, null = True (alternative int(input()))  :
# 9, 60, 08, 00006, 0
# неправильный ввод чисел :
# incorrect number input :
# +7, -9, +0, -0, -0096, +09, hgf, #$@, 9.3
#############################
# input_int(prefix=True null=True) :
# правильный ввод чисел если впепеди нет префикса но есть нули :
# correct number input if prefix = False, null = True :
# 7, 0, 00, 0098, -6, +4, -009, +03
# неправильный ввод чисел :
# incorrect number input :
# 8.9, fhf, --65, ++87, 9u6, fff, #$#, 5.3
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