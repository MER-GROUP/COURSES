names = [('max', 'red', 'alert'), ('roy', 'zob'), ('pic', 'rick', 'tick')]

def lenght(name):
	return len(''.join(name))
	
name_lenght = [lenght(i) for i in names]
print(name_lenght)

names.sort()
print(names)
#names.sort(key=lenght)
names.sort(key=lambda x: len(''.join(x)))
print(names)