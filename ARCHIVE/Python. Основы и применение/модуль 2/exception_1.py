#пример работы исключения 
def f(a, b):
	res = None
	try:
		res = a / b
		#return res
	except (TypeError, ZeroDivisionError) as e:
		print('error')
		print(e)
		print(type(e))
		print(e.args)
	else:
		print('res = ', res)
	finally:
		print('always finally')
		return res
		
print(f(5, 2))
print('------------------------------')
print(f(5, 'f'))
print('------------------------------')
print(f(5, 0))
print('------------------------------')
print(ZeroDivisionError.mro())
print('------------------------------')
print(TypeError.mro())