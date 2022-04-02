def Global():
	global temp
	temp = int
	
def fibonachi(n):
	if n in (0, 1): return 0
	elif n in (2, 3): return 1
	return fibonachi(n - 1) + fibonachi(n - 2)
	
def Main():
	for _ in range(5):
		print('-----Main()-----')
		n = int(input('введи номер последовательности фибоначи : '))
		print('элемент последовательности фибоначи =', fibonachi(n))
		
Global()
Main()