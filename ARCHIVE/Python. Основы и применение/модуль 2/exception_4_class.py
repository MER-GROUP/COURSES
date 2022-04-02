GREETING = 'Hello '
_MER_ = 'JOBBBBB'

class BadName(Exception):
	pass

def great(name):
	if name[0].isupper():
		return GREETING + name
	else:
		raise BadName(name + ' is innopropriate name')
		
__all__ = ['BadName', 'great']
		
print('import is execution')

if __name__ == '__main__':
	while True:
		try:
			name = input('enter name : ')
			greeting = great(name)
			print(greeting)
		except BadName:
			print('try again')
		else:
			break