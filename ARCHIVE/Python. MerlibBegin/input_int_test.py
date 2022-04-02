from merlib import input_int

for _ in range(3):
	d = None
	while d is None:
		print('тест #1 : input_int(text = '', prefix = True, null = False)')
		d = input_int('введи целое число : ')
	print('ты ввел :', d)
	
for _ in range(3):
	d = None
	while d is None:
		print('тест #2 : input_int(text = '', prefix = False, null = False)')
		d = input_int('введи целое число : ', prefix=False)
	print('ты ввел :', d)
	
for _ in range(3):
	d = None
	while d is None:
		print('тест #3 : input_int(text = '', prefix = False, null = True)')
		d = input_int('введи целое число : ', prefix=False, null=True)
	print('ты ввел :', d)
	
for _ in range(3):
	d = None
	while d is None:
		print('тест #4 : input_int(text = '', prefix = True, null = True)')
		d = input_int('введи целое число : ', prefix=True, null=True)
	print('ты ввел :', d)