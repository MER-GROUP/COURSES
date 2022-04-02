def g():
	print('I am function g()')
	
def f():
	print('I am function f()')
	g()
	print('I am function f()')
	
print('I am function main()')
f()
print('I am function main()')