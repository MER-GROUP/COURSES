def great(name):
	if name[0].isupper():
		return 'Hello ' + name
	else:
		raise ValueError(name + ' is innopropriate name')
		
while True:
	try:
		name = input('enter name : ')
		greeting = great(name)
		print(greeting)
	except ValueError:
		print('try again')
	else:
		break