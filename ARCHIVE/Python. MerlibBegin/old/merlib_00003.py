# правильный ввод чисел
# correct number input
# 123
# +9
# -45
# 0
# неправильный ввод чисел
# incorrect number input
# 0987
# +054
# 000
# -03
# gfdt
# _&$#g
# добавить вариант без префикса тоесть симлр без знака + и -
# вариант что если впереди много нулей вести себя как int(input())
def input_int(text = '', message = False, return_none = True):
	try:
		if message: 
			return_none = False
		digit = input(text)
		if '0' == digit[0] and 1 < len(digit):
			raise Exception
		elif digit[ : 2] in ('+0', '-0') and 2 < len(digit):
			raise Exception
		else:
			digit = int(digit)
			return digit
	except (Exception, ValueError):
		if message and return_none:
			print('включен должен быть только один булевский параметр')
		elif not message and not return_none:
			print('включен должен быть только один булевский параметр')
		else:
			return None
	
# test enter_int()
'''
print(input_int())
print(input_int(message=True))
print(input_int('введи целое число : '))
print(input_int('введи целое число : ', return_none=True))
print(input_int('введи целое число : ', message=True))
'''

def is_input_int(digit):
	pass