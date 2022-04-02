def Global():
	global temp
	temp = int
	
def FiboEl(n):
	f1, f2 = 0, 1
	while 2 < n:
		f2, f1 = f1 + f2, f2
		n -= 1
	return f1 if n in (0, 1) else f2
	
def FiboR(n):
	f1, f2 = 0, 1
	if n in (0, 1): print(f1)
	elif 2 == n: print(f1, f2, sep=' ')
	else:
		print(f1, f2, sep=' ', end=' ')
		while 2 < n:
			f2, f1 = f1 + f2, f2
			print(f2, end=' ')
			n -= 1
		print()
	
def Main():
	for _ in range(5):
		print('-----Main-----')
		n = int(input())
		el = FiboEl(n)
		print(el)
		FiboR(n)
		
Global()
Main()