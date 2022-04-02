def Global():
	global temp
	temp = int()
	
def factorial(f):
	if 0 == f:
		return 0
	elif 1 == f:
		return 1
	return f * factorial(f -1)
	
def Main():
	for i in range(7):
		print('-----Main()-----')
		print(factorial(i))
		
Global()
Main()