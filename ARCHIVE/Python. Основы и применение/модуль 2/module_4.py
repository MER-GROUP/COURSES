from exception_4_class import BadName as bad, great as gr

import exception_4_class as ext

print(ext)

'''
print(BadName)
print(great)
'''
print(bad)

def greet():
	print('hello greet()')
greet()

print(gr('Red'))