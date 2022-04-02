# примеры вызова функции
def printab(a, b):
	print(a)
	print(b)
	
print('----------')
printab(10, 20)
print('----------')
printab(a=10, b=20)
print('----------')
printab(b=20, a=10)
print('----------')
printab(10, b=20)
print('----------')
lst = [10, 20]
printab(*lst)
print('----------')
printab(lst[0], lst[1])
print('----------')
args = dict(a=10, b=20)
#args = {'a' : 10, 'b' : 20}
printab(**args)
print('----------')
printab(args['a'], args['b'])
print('----------')
printab(args.get('a'), args.get('b'))
print('----------')
printab(a=args['a'], b=args['b'])
print('----------')