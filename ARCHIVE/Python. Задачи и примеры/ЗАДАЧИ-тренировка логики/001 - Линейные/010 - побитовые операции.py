def isBin(s):
	try:
		int(s,2)
		return True
	except ValueError:
		return False

while True:
	n1=input('Binary n1 : ')
	if n1=='q':
	   break
	n2=input('Binary n2 : ')
	print(n1,n2)
	print()
	if isBin(n1) and isBin(n2):
	   n1=int(n1,2)
	   n2=int(n2,2)
	   print(n1,n2)
	   print()
	   bitOr=n1|n2
	   bitAnd=n1&n2
	   bitXor=n1^n2
	   print(bitOr)
	   print(bitAnd)
	   print(bitXor)
	   print()
	   bitOr=bin(bitOr)
	   bitAnd=bin(bitAnd)
	   bitXor=bin(bitXor)
	   print(bitOr)
	   print(bitAnd)
	   print(bitXor)
	else:
	   print('Некоректный ввод')
    