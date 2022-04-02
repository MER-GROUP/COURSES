def simple_gen():
	print('Check 1')
	yield 1
	print('Check 2')
	return 'No more alements'
	yield 2
	print('Check 3')
	
gen = simple_gen()
x = next(gen)
print(x)
y = next(gen)
print(y)
z = next(gen)