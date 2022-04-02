x = input().split()
xs = (int(i) for i in x)

def even(x):
	return 0 == x % 2
	
'''
even = filter(even, xs)
for i in even:
	print(i)
'''
'''
even2 = filter(lambda x: 0 == x % 2, xs)
for i in even2:
	print(i)
'''
even3 = list(filter(even, xs))
print(even3)