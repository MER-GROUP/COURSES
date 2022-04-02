class BadName(Exception):
	pass

def great(name):
	if name[0].isupper():
		return 'Hello ' + name
	else:
		raise BadName(name + ' is innopropriate name')
		
print(great('Anton'))
print(great('anton'))