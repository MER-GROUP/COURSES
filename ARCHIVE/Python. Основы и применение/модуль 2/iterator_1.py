my_list = [i for i in range(5)]
my_dict = dict(red = 'alert', max = 'payne', lara = 'croft')
my_str = 'hello world'

print('-----------------------')
for i in my_list:
	print(i, end=' ')
print()
print('-----------------------')
for i in my_dict:
	print(i, end=' ')
print()
print('-----------------------')
for i in my_str:
	print(i, end=' ')
print()
print('-----------------------')
iterator = iter(my_dict)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(type(iterator))
#print(next(iterator))
print('-----------------------')
it = iter(my_list)
while True:
	try:
		i = next(it)
		print(i)
	except StopIteration:
		break