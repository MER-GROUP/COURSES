import itertools as it

string = '12345'
for s in it.accumulate(string):
	print(s)
	
arr = ['10', '2', '33', '4', '55']
arr = ('10', '2', '33', '4', '55')
arr = ('10', '20', '30')
print(arr)
# for a in it.accumulate(arr, lambda x, y: [x]+[''.join(y)]):
for a in it.accumulate(arr, lambda x, y: [x]):
	print(a)
	
print('-------------------')
arr = ('10', '20', '30')
print(arr)
print(
	list(it.accumulate(
		arr, 
		# lambda x, y: (x + y)[len(x):]
		lambda x, y: [x] + [y]
	))
)
	
'''
arr = [1, 2, 3, 4, 5]
for a in it.accumulate(arr):
	print(a)
'''