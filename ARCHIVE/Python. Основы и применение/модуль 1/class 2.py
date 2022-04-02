class Counter:
	pass
	
Counter
print(Counter)
print(type(Counter))
x = Counter()
print(x)
print(type(x))
x.count = 0
x.count += 1
print(x.count)